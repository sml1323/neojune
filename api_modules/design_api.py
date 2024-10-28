import asyncio
import aiohttp
import os
from dotenv import load_dotenv


async def get_design_info(service_key, applicant, session) -> dict:
    url = "http://plus.kipris.or.kr/openapi/rest/designInfoSearchService/applicantNameSearchInfo"
    result = []
    success_count = 0
    fail_count = 0
    docs_count = 500  # 페이지당 최대 결과 수

    # 첫 요청으로 총 항목 수 확인
    request_params = {
        'accessKey': service_key,
        'applicantName': applicant,
        'startNumber': 1,
        'docsCount': docs_count,
        'etc': 'true',
        'part': 'true',
        'simi': 'true',
        'abandonment': 'true',
        'cancle': 'true',
        'destroy': 'true',
        'invalid': 'true',
        'notice': 'true',
        'open': 'true',
        'registration': 'true',
        'rejection': 'true',
        'descSort': 'true'
    }

    async with session.get(url, params=request_params, timeout=10) as response:
        content = await response.text()
        try:
            # totalCount 문자열 추출
            start = content.find("<totalCount>") + len("<totalCount>")
            end = content.find("</totalCount>")
            total_count = int(content[start:end].strip())
            max_pages = (total_count // docs_count) + (1 if total_count % docs_count else 0)
            print(f"총 검색 건수: {total_count}, 총 페이지 수: {max_pages}")
        except (ValueError, AttributeError) as e:
            print(f"totalCount를 찾을 수 없습니다. 응답 내용: {content[:200]}... 오류: {e}")
            return {"data": result}

    # 전체 페이지 순회
    page = 1
    while page <= max_pages:
        request_params['startNumber'] = page
        retry_count = 0
        max_retries = 3  # 최대 재시도 횟수

        while retry_count < max_retries:
            try:
                async with session.get(url, params=request_params, timeout=10) as response:
                    if response.status == 200:
                        content = await response.text()

                        # 빈 페이지 확인
                        if "<DesignInfo>" not in content:
                            print("더 이상 데이터가 없습니다.")
                            return {
                                "applicant": applicant,
                                "data_type": "design",
                                "data": result
                            }
                        print(f"{applicant} 페이지 {page} 호출 성공")
                        result.append(content)
                        success_count += 1
                        page += 1
                        # 요청 후 0.02초 지연
                        await asyncio.sleep(0.02)
                        break  # 성공 시 재시도 루프 종료

                    elif response.status == 404:
                        print(f"{applicant} 페이지 {page} - 데이터가 없습니다 (404)")
                        fail_count += 1
                        break
                    else:
                        print(f"{applicant} 페이지 {page}에서 HTTP 오류 발생: {response.status}")
                        fail_count += 1
                        break

            except asyncio.TimeoutError:
                retry_count += 1
                print(f"{applicant} 페이지 {page} - 시간 초과. {retry_count}/{max_retries}회 재시도 중...")
                await asyncio.sleep(1)  # 재시도 전 지연 시간 추가

            except aiohttp.ClientError as e:
                retry_count += 1
                print(f"{applicant} 페이지 {page} - 클라이언트 오류 발생: {e}. {retry_count}/{max_retries}회 재시도 중...")
                await asyncio.sleep(1)

            except Exception as e:
                print(f"{applicant} 페이지 {page}에서 알 수 없는 오류 발생: {e}")
                fail_count += 1
                break

        else:
            # 최대 재시도 횟수 초과
            print(f"{applicant} 페이지 {page} - 최대 재시도 횟수를 초과하여 실패")
            fail_count += 1
            page += 1

    print(f"총 호출 횟수: {success_count + fail_count}, 성공 횟수: {success_count}, 실패 횟수: {fail_count}")
    return {
        "applicant": applicant,
        "data_type": "design",
        "data": result
    }

async def main():
    load_dotenv()
    service_key = os.getenv('SERVICE_KEY')
    applicant = "120090148165"  # 테스트할 출원인명

    async with aiohttp.ClientSession() as session:
        result = await get_design_info(service_key, applicant, session)

# asyncio 이벤트 루프 실행
if __name__ == "__main__":
    asyncio.run(main())
