# api_modules/biz_api.py

import pandas as pd
import aiohttp
import asyncio
import xmltodict
import os
import time
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()
service_key = os.getenv('SERVICE_KEY')

# 엑세스 키와 API URL을 설정
access_key = service_key  # 실제 API 키로 변경
base_url = 'http://plus.kipris.or.kr/openapi/rest/CorpBsApplicantService/corpBsApplicantInfoV3'

# 사업자등록번호에 하이픈(-) 추가하는 함수
def format_biz_no(biz_no):
    biz_no_str = str(biz_no).zfill(10)
    return f"{biz_no_str[:3]}-{biz_no_str[3:5]}-{biz_no_str[5:]}"

# 비동기 API 호출 함수
async def fetch_applicant_info(session, biz_no, semaphore):
    async with semaphore:  # 동시 요청 제한
        formatted_biz_no = format_biz_no(biz_no)
        url = f"{base_url}?BusinessRegistrationNumber={formatted_biz_no}&accessKey={access_key}"

        # 각 요청에 대한 시간 측정
        start_time = time.time()  # 각 요청 시작 시간
        async with session.get(url) as response:
            end_time = time.time()  # 각 요청 종료 시간
            elapsed_time = end_time - start_time
            print(f"Request for biz_no {biz_no} took {elapsed_time:.2f} seconds")

            if response.status == 200:
                try:
                    response_text = await response.text()
                    response_data = xmltodict.parse(response_text)
                    items = response_data.get('response', {}).get('body', {}).get('items', None)

                    if items is None:
                        print(f"No ApplicantNumber found for biz_no {biz_no}")
                        return None
                        
                    applicant_info = items.get('corpBsApplicantInfo', {})
                    
                    # applicant_info가 문자열인 경우 처리
                    if isinstance(applicant_info, str):
                        print(f"Applicant info is a string for biz_no {biz_no}: {applicant_info}")
                        return None

                    # applicant_info가 리스트인 경우 처리
                    if isinstance(applicant_info, list):
                        # 첫 번째 항목 선택 또는 다른 로직 적용
                        applicant_info = applicant_info[0]
                        print(f"Applicant info is a list for biz_no {biz_no}, using first item.")

                    applicant_number = applicant_info.get('ApplicantNumber', 'N/A')
                    if applicant_number == 'N/A':
                        print(f"ApplicantNumber is 'N/A' for biz_no {biz_no}")
                        return None
                    return applicant_number
                    
                except Exception as e:
                    print(f"Error parsing response for biz_no {biz_no}: {e}")
                    return None
            else:
                print(f"Error fetching data for biz_no {biz_no}, status code: {response.status}")
                return None

# ApplicantNumber 리스트를 반환하는 메인 함수
async def get_applicant_numbers(limit=None):
    # 엑셀 파일을 읽어 데이터프레임으로 변환
    data = pd.read_excel('./data/TB24_100_company_info.xlsx')

    # 'biz_no' 리스트 생성
    biz_no_list = data['biz_no'].tolist()

    semaphore = asyncio.Semaphore(40)  # 동시 요청 제한: 40개씩
    tasks = []
    
    # aiohttp 세션 생성
    async with aiohttp.ClientSession() as session:
        for index, biz_no in enumerate(biz_no_list):
            # 필요한 경우 처리할 biz_no 개수를 제한할 수 있습니다.
            if limit is not None and index >= limit:
                break
            task = fetch_applicant_info(session, biz_no, semaphore)
            tasks.append(task)

        # 모든 태스크 실행 대기
        applicant_numbers = await asyncio.gather(*tasks)
        # None이 아닌 ApplicantNumber만 필터링
        applicant_numbers = [num for num in applicant_numbers if num]
        return applicant_numbers

# 테스트를 위한 코드 (직접 실행 시에만 동작)
if __name__ == "__main__":
    start_time = time.time()  # 시작 시간 기록
    applicant_numbers = asyncio.run(get_applicant_numbers(limit=100))  # 비동기 메인 함수 실행
    end_time = time.time()  # 종료 시간 기록

    # 실행 시간 출력
    total_time = end_time - start_time
    print(f"Total execution time: {total_time:.2f} seconds")

    # ApplicantNumbers 출력
    print("ApplicantNumbers:", applicant_numbers)
