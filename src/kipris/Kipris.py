import os
import requests
import xmltodict
from dotenv import load_dotenv
load_dotenv()

import module.util as util
from module.core.KiprisParams import KiprisParams
from module.MatchData import MatchData
from module.DesingPrams import DesingPrams
from module.TrademarkParams import TrademarkParams
from module.PatentParams import PatentParams


class Kipris:
    def __init__(self, url:str, params: KiprisParams):
        self.url = url
        self.params = params

    def get_response(self) -> requests.Response:
        """
        KIPRIS API에 HTTP GET 요청을 보내고 응답을 반환하는 함수
        
        :return: API 응답 객체
        """
        return requests.get(
            url=self.url,
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



# 사용 예시
if __name__ == "__main__":
    # 환경 변수에서 서비스 키 불러오기
    service_key = os.getenv('SERVICE_KEY')
    if True:
      patentParams = PatentParams(service_key)
      patentParams.set_applicantName("120140558200")
      kipris = Kipris(util.get_kipris_api_url("patUtiModInfoSearchSevice"), patentParams)
      kipris.params
      print(kipris.get_data())


    if True:
      trademarkParams = TrademarkParams(service_key)
      trademarkParams.set_applicantName("120140558200")
      kipris = Kipris(util.get_kipris_api_url("trademarkInfoSearchService"), trademarkParams)
      print(kipris.get_data())

    if True:
      desing_prams = DesingPrams(service_key)
      desing_prams.set_applicantName("420100417169")
      kipris = Kipris(util.get_kipris_api_url("designInfoSearchService"), desing_prams)
      print(kipris.get_data())
