import os, re
from lxml import etree
from typing import List, Dict

def clean_whitespace(text: str) -> str:
    """텍스트의 여러 개 공백을 하나로 줄이고, 앞뒤 공백을 제거."""
    return re.sub(r'\s+', ' ', text).strip()

def split(text: str, seperator: str = '|') -> str:
    return text.split(seperator)

class BaseDataParser:
    def __init__(self, mapping: Dict[str, str], xml_filename: str):
        self.mapping = mapping  # 매핑 정보를 초기화
        self.file_path = self.get_file_path(xml_filename)  # XML 파일 경로 생성
        self.xml_string = self.read_xml()  # XML 파일 읽기

    def get_file_path(self, xml_filename: str) -> str:
        """주어진 XML 파일 이름을 기반으로 파일 경로를 생성하는 메서드."""
        script_dir = os.path.dirname(os.path.abspath(__file__))  # 스크립트 디렉토리 경로 얻기
        return os.path.join(script_dir, xml_filename)  # XML 파일 경로 반환

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
                            element_dict[output_key] = clean_whitespace(str(sub_element.text))
                            if(output_key == "ipr_code"): 
                                element_dict[output_key] = element_dict[output_key][:2]
                            if(output_key == "main_ipc"):
                                element_dict[output_key] = split(element_dict[output_key])[0]
                        else:
                            element_dict[output_key] = ""
                
                results.append(element_dict)  # 결과 리스트에 추가
            print(results)
            return results  # 파싱된 결과 반환
        
        except etree.XMLSyntaxError as e:
            print(f"Error: XML 구문 오류: {e}")
            return []


class PatentDataParser(BaseDataParser):
    def parse(self) -> List[Dict[str, str]]:
        return super().parse("//PatentUtilityInfo")  # PatentUtilityInfo 요소 찾기


class DesignDataParser(BaseDataParser):
    def parse(self) -> List[Dict[str, str]]:
        return super().parse("//DesignInfo")  # DesignInfo 요소 찾기


class TrademarkDataParser(BaseDataParser):
    def parse(self) -> List[Dict[str, str]]:
        return super().parse("//TradeMarkInfo")  # TradeMarkInfo 요소 찾기


def main():
    # 매핑 사전 정의
    design_mapping = {
        "ipr_seq": "",
        "applicant_no": "",
        "ipr_code": "applicationNumber", # 2글자
        "title": "articleName",
        "serial_no": "number",
        "applicant": "applicantName",
        "inventor": "inventorName",
        "agent": "agentName",
        "appl_no": "applicationNumber",
        "appl_date": "applicationDate",
        "open_no": "openNumber",
        "open_date": "openDate",
        "reg_no": "registrationNumber",
        "reg_date": "registrationDate",
        "notification_num": "publicationNumber",
        "notification_date": "publicationDate",
        "legal_status_desc": "applicationStatus",
        "image_path": "imagePath",
    }


    patent_mapping = {
        "ipr_seq": "",  # 일련번호 # 
        "applicant_no": "", # 특허고객번호
        "ipr_code": "ApplicationNumber", # 2글자
        "title": "InventionName",
        "serial_no": "SerialNumber",
        "applicant": "Applicant",
        "main_ipc": "InternationalpatentclassificationNumber",
        "appl_no": "ApplicationNumber",
        "appl_date": "ApplicationDate",
        "open_no": "OpeningNumber",
        "open_date": "OpeningDate",
        "reg_no": "RegistrationNumber",
        "reg_date": "RegistrationDate",
        "notification_num": "PublicNumber",
        "notification_date": "PublicDate",
        "legal_status_desc": "RegistrationStatus",
        "abstract": "Abstract",
        "image_path": "ThumbnailPath",
    }

    trademark_mapping = {
        "ipr_seq": "",
        "applicant_no": "",
        "ipr_code": "ApplicationNumber", # 2 글자
        "title": "Title",
        "serial_no": "SerialNumber",
        "applicant": "ApplicantName",
        "agent": "AgentName",
        "appl_no": "ApplicationNumber",
        "appl_date": "ApplicationDate",
        "notification_num": "PublicNumber",
        "notification_date": "PublicDate",
        "legal_status_desc": "ApplicationStatus",
        "image_path": "ThumbnailPath",
    }

    # XML 파일 이름 설정
    design_xml_filename = '../xml/design_data_20241028_195040.xml'  # XML 파일 경로
    patent_xml_filename = '../xml/patent_data_20241028_195040.xml'  # XML 파일 경로
    trademark_xml_filename = '../xml/trademark_data_20241028_195040.xml'  # XML 파일 경로

    if True:
        print("#### design_parser")
        design_parser = DesignDataParser(design_mapping, design_xml_filename)
        design_results = design_parser.parse()
        # print(design_results)
        print("")
        print("")

    if True:
        print("#### patent_parser")
        patent_parser = PatentDataParser(patent_mapping, patent_xml_filename)
        patent_results = patent_parser.parse()
        print(patent_results)
        print("")
        print("")

    if True:
        print("#### trademark_parser")
        trademark_parser = TrademarkDataParser(trademark_mapping, trademark_xml_filename)
        trademark_results = trademark_parser.parse()
        print(trademark_results)
        print("")
        print("")


if __name__ == "__main__":
    main()  # 메인 함수 실행
