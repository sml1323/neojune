from src.test import test


# test.run()

####### new api 실험
import asyncio
from src.new_api.change_data import fetch_content


base_url = "http://plus.kipris.or.kr/kipo-api/kipi/{type}/getChangeInfoSearch"

url_dict = {
    "patent" : "patUtiModInfoSearchSevice",
    "design" : "designInfoSearchService",
    "trademark" : "trademarkInfoSearchService"
}

url = base_url.format(type = url_dict['patent'])
result = asyncio.run(fetch_content(url))
print(len(result))

print(type(result))



####### 출원번호 -> 특허 고객 번호 알아내기 