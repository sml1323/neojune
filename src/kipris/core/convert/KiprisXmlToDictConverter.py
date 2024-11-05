import os
from lxml import etree
from typing import List, Dict
from ....util import util

class KiprisXmlToDictConverter:
    def __init__(self, mapping: Dict[str, str], xml_filename: str):
        self.mapping = mapping  # 매핑 정보를 초기화
        self.file_path = self.get_file_path(xml_filename)  # XML 파일 경로 생성
        self.xml_string = self.read_xml()  # XML 파일 읽기

    def get_file_path(self, xml_filename: str) -> str:
        """주어진 XML 파일 이름을 기반으로 파일 경로를 생성하는 메서드."""
        # script_dir = os.path.dirname(os.path.abspath(__file__))  # 스크립트 디렉토리 경로 얻기
        root = util.add_sys_path()
        print(root)
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

    def parse(self, xpath_query: str) -> List[Dict[str, str]]:
        """XML 문자열을 파싱하여 매핑된 정보를 반환하는 메서드."""
        if not self.xml_string:
            return []

        try:
            root = etree.fromstring(self.xml_string)  # XML 문자열을 파싱하여 루트 요소 얻기
            elements = root.xpath(xpath_query)  # 지정된 XPath 쿼리로 요소 찾기
            
            results = []  # 결과를 저장할 리스트

            for element in elements:
                element_dict = {}  # 기본값 설정
                # 매핑된 필드 파싱
                for output_key, xml_key in self.mapping.items():
                    if xml_key:  # 빈 매핑은 건너뛰기
                        sub_element = element.find(xml_key)
                        if sub_element is not None:
                            element_dict[output_key] = util.clean_whitespace(str(sub_element.text))
                            if(output_key == "None"): 
                                element_dict[output_key] = None
                            if(output_key == "ipr_code"): 
                                element_dict[output_key] = element_dict[output_key][:2]
                            if(output_key == "main_ipc"):
                                element_dict[output_key] = util.split(element_dict[output_key])[0]
                        else:
                            element_dict[output_key] = ""
                    elif(output_key == "applicant_id"):
                        # 부모 response 요소를 찾아서 applicant_id 가져오기
                        response = element.xpath("./ancestor::itemGrop")[0]
                        if response is not None:
                            element_dict['applicant_id'] = int(response.find('applicant_id').text) if response.find('applicant_id') is not None else ''
                
                results.append(element_dict)  # 결과 리스트에 추가
            return results  # 파싱된 결과 반환
        
        except etree.XMLSyntaxError as e:
            print(f"Error: XML 구문 오류: {e}")
            return []
