import requests
import xmltodict
import os
import logging
from dotenv import load_dotenv
import time
import aiohttp
import asyncio
import traceback
from datetime import datetime
from crud.connection import db_connect  # DB 연결 모듈 임포트
from crud.db_crud import insert_data_to_db  # 삽입 함수 임포트
from crud.db_crud import fetch_data_by_page  # fetch_data_by_page 함수 임포트

# 사업자 등록번호 -> 특허 고객번호
async def get_applicant_no(service_key, applicant_info: tuple) -> dict:
    url = "http://plus.kipris.or.kr/openapi/rest/CorpBsApplicantService/corpBsApplicantInfoV3"
    company_seq, biz_no, corp_no, biz_type, company_name = applicant_info

    request_params = {
        'accessKey': service_key,
        'BusinessRegistrationNumber': biz_no
    }

    result = None
    retries = 3  # 재시도 횟수

    for attempt in range(retries):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=request_params, timeout=20) as response: 
                    if response.status == 200:
                        api_result = xmltodict.parse(await response.text())
                        body = api_result['response']['body']['items']

                        if body is None:
                            # print(applicant_info)
                            continue

                        bs_info = body.get('corpBsApplicantInfo')

                        if type(bs_info) == list:
                            bs_info = bs_info[0]

                        if bs_info.get('CorporationNumber'):
                            result =  {
                                'applicant_no': bs_info['ApplicantNumber'],
                                'app_seq': company_seq,
                                'app_type': 'company',
                                'write_time': datetime.now()
                            }
                        return result
                    else:
                        print(f"HTTP 오류: {response.status}")
                        break

        except asyncio.TimeoutError:
            print("Timeout 오류 발생")
            await asyncio.sleep(2)

        except Exception as e:
            print(f"오류 발생: {str(e)}")
            print(traceback.format_exc())
            print(applicant_info)

        if attempt < retries - 1:
            print(f"재시도 {attempt + 1}/{retries}...")
            await asyncio.sleep(2)

    return result

async def process_applicants(service_key, applicant_info_list: list):
    print("처리 시작")
    tasks = []
    for applicant_info in applicant_info_list:
        tasks.append(get_applicant_no(service_key, applicant_info))
        await asyncio.sleep(0.02)  # 각 요청 후 20ms 대기

    results = await asyncio.gather(*tasks)

    # all_results = []

    # for result in results:
    #     if result :
    #         all_results.appen


    return results
    
if __name__ == "__main__":
    load_dotenv()

    service_key = os.getenv('SERVICE_KEY')
    result = asyncio.run(process_applicants(service_key, [(1, '220-88-87953', '110111-5518240', '법인', '(주)준소프트웨어')]))
    print(result)