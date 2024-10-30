async def main():
    load_dotenv()
    service_key = os.getenv('SERVICE_KEY')
    semaphore = asyncio.Semaphore(50)
    limit = 1
    test_apps = db_crud.fetch_data_from_db('TB24_200',['app_no', 'applicant_id'],limit)
      
    
    start_time = time.time()

    pa_dict, de_dict, tr_dict = {}, {}, {}

    async with aiohttp.ClientSession() as session:
        tasks = []
        for app_no, applicant_id in test_apps:
            task = asyncio.create_task(fetch_all_info(service_key, app_no, applicant_id, session, semaphore, pa_dict, de_dict, tr_dict))
            tasks.append(task)
        await asyncio.gather(*tasks)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"전체 호출 완료: {len(test_apps)}개 신청자 처리, 총 걸린 시간 : {elapsed_time:.2f}초")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    start = time.time()
    # data 부분만 XML 파일로 저장
    save_data_as_xml(pa_dict, f"patent_data_{timestamp}")
    save_data_as_xml(de_dict, f"design_data_{timestamp}")
    save_data_as_xml(tr_dict, f"trademark_data_{timestamp}")
    print("모든 데이터를 XML 파일로 저장 완료")
    end = time.time()
    elapsed_time = end - start
    print(f"걸린 시간: {elapsed_time}")
if __name__ == '__main__':
    pass
