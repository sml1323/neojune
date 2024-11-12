import os, asyncio, aiohttp
from lxml import etree
from dotenv import load_dotenv
import backoff

from .KiprisParam import KiprisParam
from ....util import monitoring

load_dotenv()
service_key = os.getenv('SERVICE_KEY')

logger = monitoring.setup_logger("API 호출")
logger_ori = monitoring.setup_logger_origin("origin text")


class KiprisChangeInfoFetcher:
    def __init__(self, url:str, param:KiprisParam):
        self.result = []
        self.url = url
        self.params = param

    def __backoff_hdlr(details):
        exception = details.get('exception')
        print(f"Retrying after exception: {exception}... Attempt {details['tries']}")

    @backoff.on_exception(backoff.constant, (asyncio.TimeoutError, Exception), max_tries=3, interval=10, on_backoff=__backoff_hdlr)
    async def __fetch_content(self) -> str:
        """API 호출 후 페이지 내용 반환"""

        async with aiohttp.ClientSession() as session:
            async with  session.get( self.url, params= self.params, timeout=10) as response:
                return await response.text()


    def __is_blocked_users(self, content: str=""):
        if content == "":
            return False

        root:etree = etree.fromstring(content.encode("utf-8"))
        result_msg = root.find(".//resultMsg").text

        return result_msg == "Blocked users."
        
    def __throw_error_if_blocked_users(self, content: str=""):
        if self.__is_blocked_users(content):
            raise Exception("User is blocked.")
        
    async def __handle_response(self) -> bool:
        """응답 처리 및 성공 여부 반환"""
        try:
            content = await self.__fetch_content()
            self.__throw_error_if_blocked_users(content)
            logger_ori.info(content)

            root = etree.fromstring(content.encode("utf-8"))
            trans_list_string = root.find(".//transListString").text
            self.result = trans_list_string.split("|") if trans_list_string else []
            self.result = self.result[:-1]

            return True
        except asyncio.TimeoutError:
            logger.error(f"시간오류 ")
            raise
        except Exception as e:
            logger.error(f"오류: {e}")
            raise
    
    async def get_info(self) -> list[str]:
        await self.__handle_response()

        return self.result
