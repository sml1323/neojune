import os
from typing import Dict, Optional
from lxml import etree
from typing import List, Dict
from itertools import chain
from ....util import util
from .KiprisMapper import KiprisMapper
from .KiprisConvertedDataCartridge import KiprisConvertedDataCartridge


class KiprisXmlToDictConverter:
    def __init__(
            self, mapper: KiprisMapper=KiprisMapper(), 
            data_cartridge_class:type=KiprisConvertedDataCartridge, 
            xml_filename: str=""
    ):
        self.mapper = mapper  # 매핑 정보를 초기화
        self.data_cartridge_class = data_cartridge_class
        self.file_path = self.get_file_path(xml_filename)  # XML 파일 경로 생성
        self.xml_string = self.read_xml()  # XML 파일 읽기
        self.root = etree.fromstring(self.xml_string)
        self.item_name = ""

    def get_file_path(self, xml_filename: str) -> str:
        """주어진 XML 파일 이름을 기반으로 파일 경로를 생성하는 메서드."""
        # script_dir = os.path.dirname(os.path.abspath(__file__))  # 스크립트 디렉토리 경로 얻기
        root = util.add_sys_path()
        return os.path.join(root, xml_filename)  # XML 파일 경로 반환

    def read_xml(self) -> str:
        """XML 파일을 읽고 문자열로 반환하는 메서드."""
        try:
            with open(self.file_path, 'rb') as f:
                return f.read()  # XML 파일 내용 읽기
        except FileNotFoundError:
            print(f"Error: 파일을 찾을 수 없습니다: {self.file_path}")
            return ""
        except Exception as e:
            print(f"Error: XML 파일을 읽는 중 오류 발생: {e}")
            return ""

    def __get_match_dict_item(self, data:etree.Element, item:etree.Element) -> Dict:
        res:KiprisConvertedDataCartridge = self.data_cartridge_class()
        for key, value in self.mapper:
            if key == "applicant_id":
                res[key] = self.__get_applicant_id(data, value)
            else:
                sub_element = None
                if value is not None:
                    sub_element = item.find(value)

                if sub_element is not None:
                    res[key] = self.__get_element_value(sub_element)

        return res.get_dict_with_properties()


    def __get_match_dict_items(self, data: etree.Element) -> list[Dict]:
        result = []# 기본값 설정

        items = data.xpath(f".//itemGrop/items/{self.item_name}")
        
        for item in items:
            i = self.__get_match_dict_item(data, item)
            result.append(i)

        # data.xpath(item)
        return result

    def __get_is_str_none(self, value):
        return None if value == "None" else value

    def __get_element_value(self, sub_element: Optional[etree.Element]) -> str:
        """data_key별로 처리하는 match-case문"""
        if sub_element is None:
            return None

        cleaned_text = util.clean_whitespace(str(sub_element.text))
        return self.__get_is_str_none(cleaned_text)


    def __get_applicant_id(self, element: etree.Element, data_key: str) -> str:
        """applicant_id 처리 함수"""
        applicant_id_element = element.find(data_key)
        if applicant_id_element is not None:
            return applicant_id_element.text
        else:
            return None
            
            
    # def __get_match_dict
    def parse(self, xpath_query: str = "") -> List[Dict]:
        if xpath_query == "":
            xpath_query = f".//{self.item_name}" 
        """XML 문자열을 파싱하여 매핑된 정보를 반환하는 메서드."""
        if not self.xml_string:
            return []

        try:
            datas = self.root.findall("data")
            results = []  # 결과를 저장할 리스트
            for data in datas:
                match_dict = self.__get_match_dict_items(data)
                results.append(match_dict)  # 결과 리스트에 추가
            return list(chain(*results)) # 파싱된 결과 반환
        
        except etree.XMLSyntaxError as e:
            print(f"Error: XML 구문 오류: {e}")
            return []
