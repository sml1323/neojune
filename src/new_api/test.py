import os, asyncio, aiohttp
from dotenv import load_dotenv
import backoff
import random
import logging
from datetime import datetime
import time

# api 호출
from updated_design_data import get_design_info
from updated_patent_data import get_patent_info
from updated_trademark_data import get_trademark_info

# xml 
from save_to_xml import save_data_as_xml


async def fetch_all_info(service_key,application_number, session, semaphore, pa_dict, de_dict, tr_dict, code):
    async with semaphore:
        result_patent = await get_patent_info(service_key, application_number, session, semaphore)
        result_design = await get_design_info(service_key, application_number, session, semaphore)
        result_trademark = await get_trademark_info(service_key, application_number, session, semaphore)

        pa_dict[code] = result_patent
        de_dict[code] = result_design
        tr_dict[code] = result_trademark


async def main():
    timestamp = datetime.now().strftime("%Y%m%d")
    # 로그 파일을 저장할 폴더 경로 생성
    folder_path = f"../../res/logs/{timestamp}"
    os.makedirs(folder_path, exist_ok=True)  # 폴더가 없으면 생성

    # 로그 설정
    log_file_path = f"{folder_path}/updated_count.log"
    logging.basicConfig(
        filename=log_file_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    load_dotenv()
    service_key = os.getenv('SERVICE_KEY')
    
    test_apps = [{'2020040031672': 4719}, {'2020210000007': 1696}, {'1020220021103': 6841}]
    # test_apps = [{'1020220175029': 1}, {'1020230022997': 302}, {'1020220163314': 321}, {'1020140035677': 275}] # 대학
    start_time = time.time()
    
    # 결과 저장용 딕셔너리 초기화
    pa_dict, de_dict, tr_dict = {}, {}, {}
    semaphore = asyncio.Semaphore(15)

    async with aiohttp.ClientSession() as session:
        # 모든 앱의 정보를 비동기로 가져와 딕셔너리에 저장
        tasks = []
        for app in test_apps:
            for application_number, code in app.items():
                await asyncio.sleep(0.02)
                task = fetch_all_info(service_key, application_number, session, semaphore, pa_dict, de_dict, tr_dict, code)
                tasks.append(task)

        await asyncio.gather(*tasks)
    

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"전체 호출 완료: {len(test_apps)}개 신청자 처리, 총 걸린 시간 : {elapsed_time:.2f}초")
    start = time.time()
    # save_data_as_xml 호출 예시
    patent_count = save_data_as_xml(pa_dict, "patent_data", "patent", timestamp)
    design_count = save_data_as_xml(de_dict, "design_data", "design", timestamp)
    trademark_count = save_data_as_xml(tr_dict, "trademark_data", "trademark", timestamp)

    logging.info(f"updated patent data count: {patent_count}")
    logging.info(f"updated design data count: {design_count}")
    logging.info(f"updated trademark data count: {trademark_count}")
    print("모든 데이터를 XML 파일로 저장 완료")
    end = time.time()
    elapsed_time = end - start
    print(f"걸린 시간: {elapsed_time}")


# asyncio 이벤트 루프 실행
if __name__ == "__main__":
    asyncio.run(main())