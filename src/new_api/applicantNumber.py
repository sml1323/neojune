import os, asyncio, aiohttp
from lxml import etree
from dotenv import load_dotenv
import backoff
import random
import requests
from tqdm.asyncio import tqdm_asyncio
from src.util.monitoring import setup_logger

logger = setup_logger("api 호출")

load_dotenv()
service_key = os.getenv('SERVICE_KEY')

semaphore = asyncio.Semaphore(20)

request_params = {
    'accessKey' :  service_key,
}

def __backoff_hdlr(details):
    exception = details.get('exception')
    print(f"Retrying after exception: {exception}... Attempt {details['tries']}")

@backoff.on_exception(backoff.constant, (asyncio.TimeoutError, Exception), max_tries=3, interval=10, on_backoff=__backoff_hdlr)
async def fetch_content(url, params) -> str:
    # await asyncio.sleep(0.5)
    async with semaphore:
        # await asyncio.sleep(random.uniform(0.01, 0.06))
        await asyncio.sleep(0.5)
        
        async with aiohttp.ClientSession() as session:
            logger.info("요청 성공")
            async with  session.get( url, params= params, timeout=10) as response:
                content = await response.read()
                root = etree.fromstring(content)
                applicant_number = root.find(".//ApplicantNumber").text            
                return {params['applicationNumber'] : applicant_number}
        

async def get_applicantNumber(url, applicationNumber_list:list) -> list[dict]:
    
    tasks = []
    for applicationNumber in applicationNumber_list:
        request_params['applicationNumber'] = applicationNumber
        tasks.append(asyncio.create_task(fetch_content(url, request_params)))
    responses = await tqdm_asyncio.gather(*tasks)
    return responses

