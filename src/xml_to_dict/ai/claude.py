import os
from lxml import etree
from typing import List, Dict


class PatentDataParser:
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
        with open(self.file_path, 'rb') as f:
            return f.read()  # XML 파일 내용 읽기

    def parse(self) -> List[Dict[str, str]]:
        """XML 문자열을 파싱하여 디자인 정보를 반환하는 메서드."""
        root = etree.fromstring(self.xml_string)  # XML 문자열을 파싱하여 루트 요소 얻기
        design_infos = root.xpath("//PatentUtilityInfo")  # DesignInfo 요소 찾기
        
        results = []  # 결과를 저장할 리스트
        
        for design in design_infos:
            design_dict = {}  # 기본값 설정
            
            # 매핑된 필드 파싱
            for output_key, xml_key in self.mapping.items():
                if xml_key:  # 빈 매핑은 건너뛰기
                  element = design.find(xml_key)
                  if element is not None:  # 요소가 존재하는 경우
                      design_dict[output_key] = element.text if element.text is not None else ''
                  else:  # 요소가 없을 경우
                      design_dict[output_key] = ''  # 빈 문자열로 설정
            
            results.append(design_dict)  # 결과 리스트에 추가
        
        return results  # 파싱된 결과 반환




class DesignDataParser:
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
        with open(self.file_path, 'rb') as f:
            return f.read()  # XML 파일 내용 읽기

    def parse(self) -> List[Dict[str, str]]:
        """XML 문자열을 파싱하여 디자인 정보를 반환하는 메서드."""
        root = etree.fromstring(self.xml_string)  # XML 문자열을 파싱하여 루트 요소 얻기
        design_infos = root.xpath("//DesignInfo")  # DesignInfo 요소 찾기
        
        results = []  # 결과를 저장할 리스트
        
        for design in design_infos:
            design_dict = {}  # 기본값 설정
            
            # 매핑된 필드 파싱
            for output_key, xml_key in self.mapping.items():
                if xml_key:  # 빈 매핑은 건너뛰기
                  element = design.find(xml_key)
                  if element is not None:  # 요소가 존재하는 경우
                      design_dict[output_key] = element.text if element.text is not None else ''
                  else:  # 요소가 없을 경우
                      design_dict[output_key] = ''  # 빈 문자열로 설정
            
            results.append(design_dict)  # 결과 리스트에 추가
        
        return results  # 파싱된 결과 반환




class TrademarkDataParser:
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
        with open(self.file_path, 'rb') as f:
            return f.read()  # XML 파일 내용 읽기

    def parse(self) -> List[Dict[str, str]]:
        """XML 문자열을 파싱하여 디자인 정보를 반환하는 메서드."""
        root = etree.fromstring(self.xml_string)  # XML 문자열을 파싱하여 루트 요소 얻기
        design_infos = root.xpath("//TradeMarkInfo")  # DesignInfo 요소 찾기
        
        results = []  # 결과를 저장할 리스트
        
        for design in design_infos:
            design_dict = {}  # 기본값 설정
            
            # 매핑된 필드 파싱
            for output_key, xml_key in self.mapping.items():
                if xml_key:  # 빈 매핑은 건너뛰기
                  element = design.find(xml_key)
                  if element is not None:  # 요소가 존재하는 경우
                      design_dict[output_key] = element.text if element.text is not None else ''
                  else:  # 요소가 없을 경우
                      design_dict[output_key] = ''  # 빈 문자열로 설정
            
            results.append(design_dict)  # 결과 리스트에 추가
        
        return results  # 파싱된 결과 반환



def main():
    
    # 매핑 사전 정의
    design_mapping = {
        "ipr_code": "applicationNumber",
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
        "legal_status_desc": "applicationStatus"
    }


    # TB24_patent
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

    # 매핑 사전 정의
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
    patent_xml_filename = '../xml/patent_data_20241028_195040.xml'  # XML 파일 경로
    design_xml_filename = '../xml/design_data_20241028_195040.xml'  # XML 파일 경로
    trademark_xml_filename = '../xml/trademark_data_20241028_195040.xml'  # XML 파일 경로

    # patent_parser = PatentDataParser(patent_mapping, patent_xml_filename)
    # patent_results = patent_parser.parse()
    # print(patent_results)


    # # DesignDataParser 인스턴스 생성 및 데이터 파싱
    # design_parser = DesignDataParser(design_mapping, design_xml_filename)
    # design_results = design_parser.parse()
    # # print(design_results)

    trademark_parser = TrademarkDataParser(trademark_mapping, trademark_xml_filename)
    trademark_results = trademark_parser.parse()
    print(trademark_results)




    if False:
      # 결과 출력 (검증용)
      for idx, result in enumerate(design_results, 1):
          print(f"\nDesign Entry #{idx}:")
          for key, value in result.items():
              print(f"{key}: {value}")  # 각 항목의 키와 값을 출력

if __name__ == "__main__":
    main()  # 메인 함수 실행
