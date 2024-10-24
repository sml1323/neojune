import requests
import xmltodict
import os
from dotenv import load_dotenv
import time

load_dotenv()

class KiprisObject:
    def get_dict(self) -> dict:
        return vars(self)

class KiprisParams(KiprisObject):
    def __init__(self, service_key: str):
        super().__init__()
        self.ServiceKey = service_key # api key
        self.applicantName = None # 특허 번호
        self.pageNo = 1  # 기본 페이지 번호
        self.numOfRows = 1  # 최대 페이지당 건수
    
    def prev_page(self):
        self.pageNo -= 1

    def next_page(self):
        self.pageNo += 1
    
    def goto_page(self, page_number: int):
        self.pageNo = page_number

    def set_applicantName(self, applicantName: str):
        self.applicantName = applicantName
    
    def set_num_of_rows(self, value: int):
        self.numOfRows = value



class MatchData(KiprisObject):
    def __init__(self):
        super().__init__()
        self.index = ['number', 'indexNo']
        self.title = ['articleName', 'inventionTitle', 'title']
        self.applicant = ['applicationName']
        self.inventor = ['inventorname']
        self.agent = ['agentName']
        self.appl_no = ['applicationNumber']
        self.appl_date = ['applicationDate']
        self.open_no = ['openNumber']
        self.open_date = ['openDate']
        self.reg_no = ['registerNumber']
        self.reg_date = ['registerDate']
        self.pub_no = ['publicationNumber']
        self.pub_date = ['publicationDate']
        self.legal_status_desc = ['applicationStatus', 'registerStatus']
        self.drawing = ['imagePath', 'drawing']

    def get_all_keys(arg):
        """
        객체의 모든 속성 이름을 리스트로 반환하는 함수
        
        이 함수는 주어진 객체의 모든 속성 중에서 메서드가 아니고 
        언더스코어로 시작하지 않는 속성 이름만을 추출하여 리스트로 반환합니다.
        
        :param arg: 속성을 추출할 객체
        :return: 객체의 유효한 속성 이름들의 리스트
        """
        return [attr for attr in dir(arg) if not callable(getattr(arg, attr)) and not attr.startswith("__")]
    
    def get_convert_data(self, items: dict) -> dict:
        """
        단일 아이템 딕셔너리를 MatchData 클래스의 구조에 맞게 변환하는 함수
        
        :param items: 변환할 원본 데이터 딕셔너리
        :return: MatchData 구조에 맞게 변환된 데이터 딕셔너리
        """
        data = {}
        for key in self.get_all_keys():
            data[key] = {}
            for k in getattr(self, key):
                if k in items:
                    data[key] = items[k]
        return data

    def get_convert_datas(self, items: list | dict) -> list:
        """
        단일 아이템 또는 아이템 리스트를 MatchData 구조로 변환하는 함수
        
        :param items: 변환할 원본 데이터 (딕셔너리 또는 딕셔너리 리스트)
        :return: MatchData 구조로 변환된 데이터 리스트
        """
        res = []
        if type(items) == dict:
            res.append(self.get_convert_data(items))
        else:
            for item in items:
                res.append(self.get_convert_data(item))
        return res


class Kipris:
    def __init__(self, params: KiprisParams):
        self.params = params
        pass

    def get_response(self) -> requests.Response:
        """
        KIPRIS API에 HTTP GET 요청을 보내고 응답을 반환하는 함수
        
        :return: API 응답 객체
        """
        return requests.get(
            "http://plus.kipris.or.kr/kipo-api/kipi/designInfoSearchService/getAdvancedSearch", 
            params=self.params.get_dict(), 
            timeout=10
        )
    
    def get_response_dict(self) -> dict:
        """
        API 응답을 받아 XML을 딕셔너리로 파싱하는 함수
        
        :return: 파싱된 응답 데이터 딕셔너리
        :raises Exception: HTTP 오류 발생 시
        """
        res = self.get_response()
        
        if res.status_code == 200:
            return xmltodict.parse(res.content)
        else:
            raise Exception(f"HTTP 오류: {res.status_code}")
        
    def get_body(self) -> dict:
        """
        파싱된 응답에서 'body' 부분을 추출하는 함수
        
        :return: 응답의 'body' 부분 딕셔너리
        """
        return self.get_response_dict()['response']['body']
    
    def get_item(self) -> list[dict]:
        """
        'body'에서 'items'의 'item' 리스트를 추출하는 함수
        
        :return: 'item' 리스트 또는 빈 리스트 (항목이 없는 경우)
        """
        body = self.get_body()
        if body['items']['item'] is None:
            return []
        else: 
            return body['items']['item']

    def get_data(self) -> list[MatchData]:
        """
        API에서 받은 데이터를 MatchData 객체 리스트로 변환하는 함수
        
        :return: MatchData 객체의 리스트
        """
        match_data = MatchData()
        return match_data.get_convert_datas(self.get_item())




class DesingPrams(KiprisParams):
    def __init__(self, service_key):
        super().__init__(service_key)
        self.open = 'true'
        self.rejection = 'true'
        self.destroy = 'true'
        self.cancle = 'true'
        self.notice = 'true'
        self.registration = 'true'
        self.invalid = 'true'
        self.abandonment = 'true'
        self.simi = 'true'
        self.part = 'true'
        self.etc = 'true'
        self.sortSpec = 'applicationDate'
    



# 사용 예시
if __name__ == "__main__":
    # start = time.time()

    # # 환경 변수에서 서비스 키 불러오기
    service_key = os.getenv('SERVICE_KEY')

    desing_prams = DesingPrams(service_key)
    desing_prams.set_applicantName("420100417169")
    kipris = Kipris(desing_prams)
    print(kipris.get_data())
    print("=========")
    desing_prams.numOfRows = 1
    print(kipris.get_data())
    # print(kipris.get_data())
    # desing_prams.add_page()
    # print(kipris.get_data())