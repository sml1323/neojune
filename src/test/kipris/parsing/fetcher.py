import os, asyncio
from ....kipris.core.parsing.KiprisFetcher import KiprisFetcher
from ....kipris.core.parsing.KiprisParam import KiprisParam

class KiprisDesignPram(KiprisParam):
    def __init__(self, app_no, applicant_id):
        super().__init__(app_no, applicant_id)
        self.applicantName = app_no
        self.startNumber = 1
        self.etc = 'true'
        self.part = 'true'
        self.simi = 'true'
        self.abandonment = 'true'
        self.cancle = 'true'
        self.destroy = 'true'
        self.invalid = 'true'
        self.notice = 'true'
        self.open = 'true'
        self.registration = 'true'
        self.rejection = 'true'
        self.descSort = 'true'
    
def main():
    param = KiprisDesignPram(120080091393, 10)
    print(param.get_dict())
    # 출력 결과
    # {'accessKey': 'gT7qoU0dWQGE2pCd0zkrhnxsvaBXkljFsa=s9/vbar0=', 'docsCount': 500, 'applicantName': 120080091393, 'startNumber': 1, 'etc': 'true', 'part': 'true', 'simi': 'true', 'abandonment': 'true', 'cancle': 'true', 'destroy': 'true', 'invalid': 'true', 'notice': 'true', 'open': 'true', 'registration': 'true', 'rejection': 'true', 'descSort': 'true'}
    
    url = "http://plus.kipris.or.kr/openapi/rest/designInfoSearchService/applicantNameSearchInfo"
    fetcher = KiprisFetcher(url, [ param ])

    res = asyncio.run(fetcher.get_infos())

    print(vars(res[0]))
    # 출력 결과
    """
    {
        'applicant_number': 120080091393, 'applicant_id': 10, 'xml_str_list': [
            '<?xml version="1.0" encoding="UTF-8"?>생략......',
        ]
    }
    """


