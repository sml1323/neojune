import os, asyncio, aiohttp
from lxml import etree
from dotenv import load_dotenv
import backoff
import random

from .KiprisFetchData import KiprisFetchData
from .KiprisParam import KiprisParam
from ...core.parsing import KiprisFetcher
from ....util import monitoring
from ....test.prometheus.prometheus import PrometheusDashboard

load_dotenv()
service_key = os.getenv('SERVICE_KEY')

logger = monitoring.setup_logger("API 호출")
logger_ori = monitoring.setup_logger_origin("origin text")

class KiprisApplicantInfoFetcher:
    def __init__(self, url:str, param:KiprisParam):
        self.result = []
        self.url = url
        self.max_pages = 0
        self.success_count = 0
        self.fail_count = 0
        self.session = None
        self.params = param

    async def __open_session(self):
        """ClientSession을 열어서 여러 요청에서 공유"""
        if self.session is None:
            self.session = aiohttp.ClientSession()

    async def __close_session(self):
        """ClientSession을 닫음"""
        if self.session:
            await self.session.close()
            self.session = None

    def __backoff_hdlr(details):
        exception = details.get('exception')
        print(f"Retrying after exception: {exception}... Attempt {details['tries']}")

    @backoff.on_exception(backoff.constant, (asyncio.TimeoutError, Exception), max_tries=3, interval=10, on_backoff=__backoff_hdlr)
    async def __fetch_content(self, page: int) -> str:
        """API 호출 후 페이지 내용 반환"""
        self.params.docsStart = page
        async with KiprisFetcher.semaphore:
            async with KiprisFetcher.rate_limiter:
                logger.info("호출 요청") 
                self.prometheus.api_counter_plus()
                async with self.session.get(self.url, params=self.params.get_dict(), timeout=10) as response:
                    result = await response.text()
                    self.prometheus.api_response_time()
                    return result

    def __get_total_count(self, content: str) -> int:
        """lxml을 사용하여 XML 응답에서 totalCount 또는 TotalSearchCount 값을 추출"""
        root = etree.fromstring(content.encode("utf-8"))

        for tag in ["totalCount", "TotalSearchCount"]:
            element = root.find(f".//{tag}")
            if element is not None and element.text.isdigit():
                return int(element.text)

        print("totalCount와 TotalSearchCount를 찾을 수 없습니다.")
        return 0

    def __is_blocked_users(self, content: str=""):
        if content == "":
            return False

        root:etree = etree.fromstring(content.encode("utf-8"))
        result_msg = root.find(".//resultMsg").text

        return result_msg == "Blocked users."
        
    def __throw_error_if_blocked_users(self, content: str=""):
        if self.__is_blocked_users(content):
            raise Exception("User is blocked.")
        
    
    def __get_max_pages(self, total_count: int):
        """총 페이지 수 계산"""
        return (total_count // self.params.docsCount) + (1 if total_count % self.params.docsCount else 0)

    async def __handle_response(self, page: int) -> bool:
        """응답 처리 및 성공 여부 반환"""
        try:
            content = await self.__fetch_content(page)
            self.__throw_error_if_blocked_users(content)
            logger_ori.info(content)

            if page == 1:  # 첫 페이지는 totalCount 추출
                total_count = self.__get_total_count(content)
                if total_count == -1:
                    return False # totalCount 추출 실패시 함수 종료
                self.max_pages = self.__get_max_pages(total_count)
                # logger.info(f"총 검색 건수: {total_count}, 총 페이지 수: {self.max_pages}")
            self.result.append(content)
            self.success_count += 1
            logger.info(f"{self.params.app_no} 페이지 {page} 호출 성공")
            return True
        except asyncio.TimeoutError:
            logger.error(f"{self.params.app_no}, 페이지 {page}에서 시간 초과 오류")
            self.fail_count += 1
            raise
        except Exception as e:
            print(f"{self.params.app_no} 페이지 {page}에서 오류: {e}")
            self.fail_count += 1
            raise

    async def __increment_page(self, page: int) -> int:
        """페이지 증가 및 지연 적용"""
        await asyncio.sleep(0.02)
        return page + self.params.docsCount

    async def __fetch_initial(self):
        """첫 요청으로 totalCount 추출 및 첫 페이지 결과 저장"""
        success = await self.__handle_response(1)
        if not success:
            print("첫 페이지 요청 실패")

    async def __fetch_pages(self):
        
        tasks = []
        # 페이지 번호 2부터 self.max_pages까지 반복
        page = 1+ self.params.docsCount
        while page <= self.max_pages:
            # _increment_page를 사용하여 페이지를 증가시키면서 지연을 적용
            task = self.__handle_response(page)
            tasks.append(task)
            page = await self.__increment_page(page)

        # 모든 task를 asyncio.gather로 실행
        await asyncio.gather(*tasks)

        # 최종 결과 출력
        total_requests = self.success_count + self.fail_count
        logger.info(f"총 호출 횟수: {total_requests}, 성공: {self.success_count}, 실패: {self.fail_count}")

    
    async def get_info(self, session: aiohttp.ClientSession = None, prometheus:PrometheusDashboard = None) -> KiprisFetchData:
        self.prometheus:PrometheusDashboard = prometheus
        if session is None:
            await self.__open_session()
            await self.__fetch_initial()
            await self.__fetch_pages()
            await self.__close_session()
        elif session is not None and self.prometheus is not None:
            self.session = session
            await self.__fetch_initial()
            await self.__fetch_pages()

        
        return KiprisFetchData(self.params.app_no, self.params.applicant_id, self.result)



async def main():
    applicant = "120140558200"
    kipris_applicant_info_fetcher = KiprisApplicantInfoFetcher()
    async with aiohttp.ClientSession() as session:
        result = await kipris_applicant_info_fetcher.get_info(applicant, session)

if __name__ == "__main__":
    asyncio.run(main())
