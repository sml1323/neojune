import asyncio
import aiohttp
import xmltodict
import os
from dotenv import load_dotenv
async def get_trademark_info(service_key, applicant, session) -> list[dict]:
    url = "http://plus.kipris.or.kr/kipo-api/kipi/trademarkInfoSearchService/getAdvancedSearch"

    page = 1
    result = []

    while True:
        request_params = {
            'ServiceKey': service_key,
            'applicantName': applicant,
            'freeSearch': applicant,
            'application': 'true',
            'registration': 'true',
            'refused': 'true',
            'expiration': 'true',
            'withdrawal': 'true',
            'publication': 'true',
            'cancel': 'true',
            'abandonment': 'true',
            'serviceMark': 'true',
            'trademark': 'true',
            'trademarkServiceMark': 'true',
            'businessEmblem': 'true',
            'collectiveMark': 'true',
            'internationalMark': 'true',
            'character': 'true',
            'figure': 'true',
            'compositionCharacter': 'true',
            'figureComposition': 'true',
            'sound': 'true',
            'fragrance': 'true',
            'color': 'true',
            'dimension': 'true',
            'colorMixed': 'true',
            'hologram': 'true',
            'motion': 'true',
            'visual': 'true',
            'invisible': 'true',
            'pageNo': page,
            'numOfRows': 500,
            'sortSpec': 'applicationDate',
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
                            'title': item.get('title'),
                            'applicant': item.get('applicationName'),
                            'agent': item.get('agentName'),
                            'appl_no': item.get('applicationNumber'),
                            'appl_date': item.get('applicationDate'),
                            'reg_no': item.get('registerNumber'),
                            'reg_date': item.get('registerDate'),
                            'pub_no': item.get('publicationNumber'),
                            'pub_date': item.get('publicationDate'),
                            'legal_status_desc': item.get('applicationStatus'),
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
