import asyncio, aiohttp
from .KiprisFetchData import KiprisFetchData
from .KiprisApplicantInfoFetcher import KiprisApplicantInfoFetcher
from .KiprisParam import KiprisParam
from tqdm import tqdm
from ....util import monitoring
import backoff
from ....util.util import yappi_profiler
import random
from lxml import etree

semaphore = asyncio.Semaphore(20)
logger = monitoring.setup_logger("API 호출")

class KiprisApplicantDaliyFetcher(KiprisApplicantInfoFetcher):
    def __init__(self, url:str, param):
        super().__init__(url, param)

        self.result = None
        self.url = url
        self.params = param

    def backoff_hdlr_wrapper(self, details):
        """super()로 상위 클래스의 backoff_hdlr을 호출하는 래퍼 함수"""
        super().backoff_hdlr(details)

    @backoff.on_exception(backoff.constant, (asyncio.TimeoutError, Exception), max_tries=3, interval=10, on_backoff=backoff_hdlr_wrapper)
    async def fetch_content(self) -> str:
        while True:
            if semaphore._value <= 10:
                logger.debug(f"재시도 : {self.params.applicationNumber}, semaphore : {semaphore._value} ")
                await asyncio.sleep(1)
            async with semaphore:
                await asyncio.sleep(0.5)
                logger.info("호출 성공") 
                await asyncio.sleep(random.uniform(0.01, 0.06))
                async with self.session.get(self.url, params=self.params.get_dict(), timeout=10) as response:
                    return await response.text()

    async def handle_response(self) -> bool:
        """응답 처리 및 성공 여부 반환"""
        try:
            content = await self.fetch_content()
            self.throw_error_if_blocked_users(content)

            root = etree.fromstring(content.encode("utf-8"))
            
            applicant_number_b = root.find(".//ApplicantNumber")
            if applicant_number_b is None:
                applicant_number_b = root.find(".//applicantCode")
            if applicant_number_b is not None:
                self.result =  {self.params.applicationNumber : applicant_number_b.text}
        except asyncio.TimeoutError:
            logger.error(f"시간오류 ")
            raise
        except Exception as e:
            logger.error(f"오류: {e}")
            raise

    async def get_info(self, session: aiohttp.ClientSession = None):
        if session is None:
            await self.open_session()
            await self.handle_response()
            await self.close_session()
        else:
            self.session = session
            await self.handle_response()

        return self.result

class KiprisApplicantFetcher:
    def __init__(self, url:str='', params:list[KiprisParam]=[KiprisParam()]):
        self.url = url
        self.params = params
        self.result = None

    async def __task(self, param: KiprisParam, session: aiohttp.ClientSession):
        info = KiprisApplicantDaliyFetcher(self.url, param)
        result = await info.get_info(session)  # session 전달
        return result
    
    async def get_infos(self, file_name: str = "default.prof") -> list:
        # 여기서 yappi_profiler를 동적으로 적용하여 호출
        base_path = "res/log"
        profiled_get_infos = yappi_profiler(f'{base_path}/{file_name}')(self.__get_infos)
        return await profiled_get_infos()

    async def __get_infos(self) -> list:
        tasks = []
        async with aiohttp.ClientSession() as session: 
            for param in self.params:
                task = asyncio.create_task(self.__task(param, session)) 
                tasks.append(task)

            self.result  = await asyncio.gather(*tasks)
            return self.result 
    
    def set_params(self, params_list:list[str|int], ParamType):
        res = []
        for params in params_list:
            res.append(ParamType(params))
        self.params = res

    def applicant_list_db(self, db_dict)-> list[list]:
        db_in_list = []
        for data in self.result:
            # data.items() -> key : 출원번호 / value : 특허고객번호
            # db_dict -> key : 특허 고객번호 / value  : auto id
            key, value = list(data.items())[0]

            if value in db_dict:
                db_in_list.append([key, db_dict[value]])

        return db_in_list

