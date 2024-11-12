"http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/patentApplicantInfo?applicationNumber=1020060118886&accessKey=write your key"


from ..util.util import get_timestamp
# from src.util.util import get_timestamp

import os, asyncio, aiohttp
from lxml import etree
from dotenv import load_dotenv
import backoff
import random

load_dotenv()
service_key = os.getenv('SERVICE_KEY')

appl_no = None

request_params = {
    'accessKey' :  service_key,
    'applicationNumber' : appl_no
}

def __backoff_hdlr(details):
    exception = details.get('exception')
    print(f"Retrying after exception: {exception}... Attempt {details['tries']}")

@backoff.on_exception(backoff.constant, (asyncio.TimeoutError, Exception), max_tries=3, interval=10, on_backoff=__backoff_hdlr)
async def fetch_content(url, appl_no) -> str:
    """API 호출 후 페이지 내용 반환"""
    
    async with aiohttp.ClientSession() as session:
        async with  session.get( url, params= request_params, timeout=10) as response:
            content = await response.read()
            # XML 파싱
            root = etree.fromstring(content)
            applicant_number = root.find(".//ApplicantNumber").text
            # appl_no : 출원 번호 / applicant_number : 해당 출원번호에 맞는 특허고객번호 
            return {appl_no : applicant_number}