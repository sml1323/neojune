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

def __backoff_hdlr(details):
    exception = details.get('exception')
    print(f"Retrying after exception: {exception}... Attempt {details['tries']}")

@backoff.on_exception(backoff.constant, (asyncio.TimeoutError, Exception), max_tries=3, interval=10, on_backoff=__backoff_hdlr)
async def fetch_content(url, params) -> str:
    # await asyncio.sleep(0.5)
    
    while True:
        # print(semaphore._value)
        if semaphore._value <= 10:
            logger.debug(f"재시도 : {params['applicantionNumber']}, semaphore : {semaphore._value} ")
            await asyncio.sleep(1)
        async with semaphore:
            await asyncio.sleep(0.5)
            
            async with aiohttp.ClientSession() as session:
                logger.info(f"요청 성공 , semaphore : {semaphore._value}")
                # print(f"성공 {params['applicationNumber']}")
                async with  session.get( url, params= params, timeout=10) as response:
                    content = await response.read()
                    root = etree.fromstring(content)
                    applicant_number_b = root.find(".//ApplicantNumber")
                    if applicant_number_b is not None:
                        return  {params['applicationNumber'] : applicant_number_b.text}
                    else:
                        print(params)
                        print(etree.tostring(root, pretty_print=True, encoding='unicode'))
                        return None
                    # print("응답후 ", semaphore._value,params['applicationNumber'] )           
    

async def get_applicantNumber(url, applicationNumber_list:list) -> list[dict]:
    
    tasks = []
    for applicationNumber in applicationNumber_list:
        request_params = {
            'accessKey' :  service_key,
            'applicationNumber' : applicationNumber
        }
        tasks.append(asyncio.create_task(fetch_content(url, request_params)))
    responses = await tqdm_asyncio.gather(*tasks)
    return responses



# # 메인 함수
# async def main():
#     application_number_list = ['123456', '789101', '112233', '445566', '778899']  # 예시
#     await get_applicantNumber("your_url", application_number_list)

# # 실행
# asyncio.run(main())