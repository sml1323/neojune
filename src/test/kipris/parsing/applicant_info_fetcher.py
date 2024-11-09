import os, asyncio
from ....kipris.core.parsing.KiprisApplicantInfoFetcher import KiprisApplicantInfoFetcher
from ....kipris.core.parsing.KiprisParam import KiprisParam
from ....kipris.parsing.params.KiprisDesignPram import KiprisDesignPram

    
def main():
    param = KiprisDesignPram(120080091393, 10)
    print(param.get_dict())
    # 출력 결과
    # {'accessKey': 'gT7qoU0dWQGEjkljsdfjFsa=s9/vbar0=', 'docsCount': 500, 'applicantName': 120080091393, 'startNumber': 1, 'etc': 'true', 'part': 'true', 'simi': 'true', 'abandonment': 'true', 'cancle': 'true', 'destroy': 'true', 'invalid': 'true', 'notice': 'true', 'open': 'true', 'registration': 'true', 'rejection': 'true', 'descSort': 'true'}
    
    url = "http://plus.kipris.or.kr/openapi/rest/designInfoSearchService/applicantNameSearchInfo"
    fetcher = KiprisApplicantInfoFetcher(url, param)

    res = asyncio.run(fetcher.get_info())

    print(vars(res))
    # 출력 결과
    """
    {
        'applicant_number': 120080091393, 'applicant_id': 10, 'xml_str_list': [
            '<?xml version="1.0" encoding="UTF-8"?>생략......',
        ]
    }
    """


