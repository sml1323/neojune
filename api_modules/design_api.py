import asyncio
import aiohttp
import os
from dotenv import load_dotenv


# 로그 설정

async def get_design_info(service_key, applicant, session) -> dict:
    url = "http://plus.kipris.or.kr/openapi/rest/designInfoSearchService/applicantNameSearchInfo"
    result = []
    success_count = 0
    fail_count = 0
    docs_count = 500  # 페이지당 최대 결과 수

    # 총 항목 수 확인을 위한 첫 요청
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
            # totalCount 문자열 검색
            start = content.find("<totalCount>") + len("<totalCount>")
            end = content.find("</totalCount>")
            total_count = int(content[start:end].strip())
            max_pages = (total_count // docs_count) + (1 if total_count % docs_count else 0)
            print(f"총 검색 건수: {total_count}, 총 페이지 수: {max_pages}")
            result.append(content)
            success_count += 1
        except ValueError:
            print("totalCount를 찾을 수 없습니다.")
            return result
    # 전체 페이지 순회

    page = 2
    while page <= max_pages:
        request_params['startNumber'] = page
        try:
            async with session.get(url, params=request_params, timeout=10) as response:
                if response.status == 200:
                    content = await response.text()
                    print(f"{applicant} 페이지 {page} 호출 성공")
                    result.append(content)  # 파싱하지 않고 content 자체를 추가
                    success_count += 1
                    page += 1
                    await asyncio.sleep(0.02)  # 다음 요청 전 지연 시간 추가
                else:
                    print(f"{applicant} 페이지 {page} HTTP 오류: {response.status}")
                    fail_count += 1
                    break
        except asyncio.TimeoutError:
            print(f"{applicant} 페이지 {page}에서 시간 초과 오류, 재시도 중...")
            await asyncio.sleep(1)
            fail_count += 1
            continue
        except Exception as e:
            print(f"{applicant} 페이지 {page}에서 오류: {e}")
            fail_count += 1
            break

    print(f"총 호출 횟수: {success_count + fail_count}, 성공 횟수: {success_count}, 실패 횟수: {fail_count}")
    return result

async def main():
    load_dotenv()
    service_key = os.getenv('SERVICE_KEY')
    applicant = "120090148165"  # 테스트할 출원인명

    async with aiohttp.ClientSession() as session:
        result = await get_design_info(service_key, applicant, session)
        print(result)

# asyncio 이벤트 루프 실행
if __name__ == "__main__":
    asyncio.run(main())
