import asyncio
import aiohttp
import xmltodict
import os
from dotenv import load_dotenv
async def get_patent_info(service_key, applicant, session) -> list[dict]:
    url = "http://plus.kipris.or.kr/kipo-api/kipi/patUtiModInfoSearchSevice/getAdvancedSearch"

    page = 1
    result = []

    while True:
        request_params = {
            'ServiceKey': service_key,
            'applicant': applicant,
            'pageNo': page,
            'numOfRows': 500,
        }

        try:
            async with session.get(url, params=request_params, timeout=10) as response:
                if response.status == 200:
                    content = await response.text()
                    api_result = xmltodict.parse(content)
                    body = api_result['response']['body']['items']

                    if not body:
                        break

                    items = body['item']
                    if isinstance(items, dict):
                        items = [items]

                    for item in items:
                        result.append({
                            'index': item.get('indexNo'),
                            'title': item.get('inventionTitle'),
                            'applicant': item.get('applicationName'),
                            'appl_no': item.get('applicationNumber'),
                            'appl_date': item.get('applicationDate'),
                            'open_no': item.get('openNumber'),
                            'open_date': item.get('openDate'),
                            'reg_no': item.get('registerNumber'),
                            'reg_date': item.get('registerDate'),
                            'pub_no': item.get('publicationNumber'),
                            'pub_date': item.get('publicationDate'),
                            'legal_status_desc': item.get('registerStatus'),
                            'drawing': item.get('drawing'),
                        })
                    page += 1
                else:
                    print(f"HTTP Error: {response.status}")
                    break
        except asyncio.TimeoutError:
            print(f"Timeout error on page {page}, retrying...")
            await asyncio.sleep(2)
            continue
        except Exception as e:
            print(f"Error: {e} on page {page}")
            break

    return result