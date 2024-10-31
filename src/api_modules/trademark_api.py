import asyncio
import aiohttp
import os
import time
from dotenv import load_dotenv
from monitoring.logging import setup_logger
from monitoring.prometheus import API_CALL_COUNT, API_RESPONSE_TIME

logger = setup_logger('trademark')

async def get_trademark_info(service_key, applicant, session) -> dict:
    url = "http://plus.kipris.or.kr/openapi/rest/trademarkInfoSearchService/applicantNamesearchInfo"
    result = []
    success_count = 0
    fail_count = 0
    docs_count = 500  # 페이지당 최대 결과 수

    # 첫 요청으로 총 항목 수 확인 및 페이지 수 계산
    request_params = {
        'accessKey': service_key,
        'applicantName': applicant,
        'docsStart': 1,
        'docsCount': docs_count,
        'abandonment': 'true',
        'application': 'true',
        'cancel': 'true',
        'expiration': 'true',
        'publication': 'true',
        'refused': 'true',
        'registration': 'true',
        'withdrawal': 'true',
        'businessEmblem': 'true',
        'certMark': 'true',
        'collectiveMark': 'true',
        'geoCertMark': 'true',
        'geoOrgMark': 'true',
        'internationalMark': 'true',
        'serviceMark': 'true',
        'trademark': 'true',
        'trademarkServiceMark': 'true',
        'character': 'true',
        'compositionCharacter': 'true',
        'figure': 'true',
        'figureComposition': 'true',
        'fragrance': 'true',
        'sound': 'true',
        'color': 'true',
        'colorMixed': 'true',
        'dimension': 'true',
        'hologram': 'true',
        'invisible': 'true',
        'motion': 'true',
        'visual': 'true',
        'descSort': 'true'
    }

    # 총 항목 수 확인을 위한 첫 요청
    logger.info(f"{applicant} 페이지 1 호출 성공")
    API_CALL_COUNT.inc()
    start_time = time.time()
    async with session.get(url, params=request_params, timeout=10) as response:
        content = await response.text()
        API_RESPONSE_TIME.observe(time.time() - start_time) 
        try:
            # totalCount 문자열 검색
            start = content.find("<TotalSearchCount>") + len("<TotalSearchCount>")
            end = content.find("</TotalSearchCount>")
            total_count = int(content[start:end].strip())
            max_pages = (total_count // docs_count) + (1 if total_count % docs_count else 0)
            print(f"총 검색 건수: {total_count}, 총 페이지 수: {max_pages}")
            result.append(content)
            success_count += 1
        except (ValueError, AttributeError) as e:
            print(f"totalCount를 찾을 수 없습니다. 응답 내용: {content[:200]}... 오류: {e}")
            return result

    # 전체 페이지 순회
    page = 2 
    while page <= max_pages:
        request_params['docsStart'] = page
        retry_count = 0
        max_retries = 3  # 최대 재시도 횟수

        while retry_count < max_retries:
            try:
                logger.info(f"{applicant} 페이지 {page} 호출 성공")
                async with session.get(url, params=request_params, timeout=10) as response:
                    if response.status == 200:
                        content = await response.text()

                        # 빈 페이지 확인
                        if "<TradeMarkInfo>" not in content:
                            print("더 이상 데이터가 없습니다.")
                            return {
                                "applicant": applicant,
                                "data_type": "trademark",
                                "data": result
                            }
                        
                        result.append(content) 
                        success_count += 1
                        page += 1
                        # 요청을 보낸 후 0.02초 지연
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
    return result

async def main():
    load_dotenv()
    service_key = os.getenv('SERVICE_KEY')
    applicant = "120140558200"  # 테스트할 출원인명

    async with aiohttp.ClientSession() as session:
        result = await get_trademark_info(service_key, applicant, session)
    print(result)

# asyncio 이벤트 루프 실행
if __name__ == "__main__":
    asyncio.run(main())

