import os
import requests
import xmltodict
from dotenv import load_dotenv
load_dotenv()

import module.util as util
from module.core.KiprisParams import KiprisParams

from module.KiprisBackFileDataGenerator import KiprisBackFileDataGenerator

from module.params.DesingPrams import DesingPrams
from module.backfile_prop.DesingBackFileDataKeyProp import DesingBackFileDataKeyProp

from module.params.TrademarkParams import TrademarkParams
from module.backfile_prop.TrademarkBackFileDataKeyProp import TrademarkBackFileDataKeyProp

from module.params.PatentParams import PatentParams
from module.backfile_prop.PatentBackFileDataKeyProp import PatentBackFileDataKeyProp


class Kipris:
    def __init__(self, params: KiprisParams):
        self.params = params

    def get_response(self, applicant) -> requests.Response:
        """
        KIPRIS API에 HTTP GET 요청을 보내고 응답을 반환하는 함수
        
        :return: API 응답 객체
        """
        self.params.set_applicantName(applicant)

        params = self.params.get_dict()
        params['pageNo'] = self.params.pageNo
        params['numOfRows'] = self.params.numOfRows

        return requests.get(
            url=util.get_kipris_api_url(self.params.serviceName),
            params=params, 
            timeout=10
        )

    
    def get_response_dict(self, applicant) -> dict:
        """
        API 응답을 받아 XML을 딕셔너리로 파싱하는 함수
        
        :return: 파싱된 응답 데이터 딕셔너리
        :raises Exception: HTTP 오류 발생 시
        """
        res = self.get_response(applicant)
        
        if res.status_code == 200:
            return xmltodict.parse(res.content)
        else:
            raise Exception(f"HTTP 오류: {res.status_code}")
        
    def get_body(self, applicant) -> dict:
        """
        파싱된 응답에서 'body' 부분을 추출하는 함수
        
        :return: 응답의 'body' 부분 딕셔너리
        """
        return self.get_response_dict(applicant)['response']['body']
    
    def get_item(self, applicant) -> list[dict]:
        """
        'body'에서 'items'의 'item' 리스트를 추출하는 함수
        
        :return: 'item' 리스트 또는 빈 리스트 (항목이 없는 경우)
        """
        body = self.get_body(applicant)
        if body['items']['item'] is None:
            return []
        else: 
            item = body['items']['item']
            if isinstance(item, dict):
                item = [item]
            return item


    def prev_page(self):
        """현재 페이지 번호를 1 감소시킵니다."""
        self.params.pageNo -= 1

    def next_page(self):
        """현재 페이지 번호를 1 증가시킵니다."""
        self.params.pageNo += 1

    def goto_page(self, page_number: int):
        """현재 페이지 번호를 지정된 페이지 번호로 설정합니다."""
        self.params.pageNo = page_number



# 사용 예시
if __name__ == "__main__":
    if True:
        patent_prams = PatentParams()
        kipris = Kipris(patent_prams)
        item = kipris.get_item("120160255942")
        
        patent_backfile_data_key_prop = PatentBackFileDataKeyProp()
        backfile_data_generator = KiprisBackFileDataGenerator(patent_prams, patent_backfile_data_key_prop)
        print(backfile_data_generator.create(item))


    if True:
        trademark_prams = TrademarkParams()
        kipris = Kipris(trademark_prams)
        item = kipris.get_item("120140558200")
        
        trademark_backfile_data_key_prop = TrademarkBackFileDataKeyProp()
        backfile_data_generator = KiprisBackFileDataGenerator(trademark_prams, trademark_backfile_data_key_prop)
        print(backfile_data_generator.create(item))

    if True:
        desing_prams = DesingPrams()
        kipris = Kipris(desing_prams)
        item = kipris.get_item("420100417169")
        
        desing_backfile_data_key_prop = DesingBackFileDataKeyProp()
        backfile_data_generator = KiprisBackFileDataGenerator(desing_prams, desing_backfile_data_key_prop)
        print(backfile_data_generator.create(item))