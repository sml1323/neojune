# 변동정보 api 3가지 특허/실용신안, 디자인, 상표 받아오기
# 출원번호를 리스트형식으로 리턴

from ..util.util import get_timestamp
# from src.util.util import get_timestamp

import os, asyncio, aiohttp
from lxml import etree
from dotenv import load_dotenv
import backoff
import random

load_dotenv()
service_key = os.getenv('SERVICE_KEY')
today = get_timestamp()

## change patent data

base_url = "http://plus.kipris.or.kr/kipo-api/kipi/{type}/getChangeInfoSearch"

url_dict = {
    "patent" : "patUtiModInfoSearchSevice",
    "design" : "designInfoSearchService",
    "trademark" : "trademarkInfoSearchService"
}

request_params = {
    'ServiceKey' :  service_key,
    'date' : today
}

def __backoff_hdlr(details):
    exception = details.get('exception')
    print(f"Retrying after exception: {exception}... Attempt {details['tries']}")

@backoff.on_exception(backoff.constant, (asyncio.TimeoutError, Exception), max_tries=3, interval=10, on_backoff=__backoff_hdlr)
async def fetch_content(url) -> str:
    """API 호출 후 페이지 내용 반환"""
    async with aiohttp.ClientSession() as session:
        async with  session.get( url, params= request_params, timeout=10) as response:
            content = await response.read()
            # XML 파싱
            root = etree.fromstring(content)
            trans_list_string = root.find(".//transListString").text
            # 출원번호 리스트 생성
            trans_list = trans_list_string.split("|") if trans_list_string else []
            return trans_list[:-1]

# async def fetch_all_data() -> list:
#     """모든 URL에 비동기로 요청을 보내고 출원번호를 리스트 형식으로 반환"""

#     tasks = []
#     for property, url_parse in url_dict.items():
#         url = base_url.format(type = url_parse)
#         tasks.append(asyncio.create_task(fetch_content(url, property)))

#     responses = await asyncio.gather(*tasks) 
#     return responses