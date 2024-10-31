import os
import xml.etree.ElementTree as ET
from ..util import util



class XmlApplicanIdRegistor:
    def __init__(self):
        # XML 루트 요소 생성
        self.root = ET.Element("responseData")
        self.response_elem = ET.SubElement(self.root, "response")
        self.applicant_tag = ET.SubElement(self.response_elem, "applicant_id")
        self.header = ET.SubElement(self.response_elem, "header")
        self.body = ET.SubElement(self.response_elem, "body")
        self.items_elem = ET.SubElement(self.body, "items")
        self.items: ET.SubElement = None
        self.tree = ET.ElementTree(self.root)

    def __append_item(self):
        if self.items is not None:
                for elem in self.items:
                    self.items_elem.append(elem)
        

    def __append_items_from_xml_strings(self, data):
        # data 내부에 있는 XML 콘텐츠를 <items>에 추가
        for content in data:
            original_data = ET.fromstring(content)

            # 기존 XML에서 <items> 내부 태그들만 추가
            self.items = original_data.find(".//items")
            self.__append_item()

    def __applican_id_regist(self, applicant_id, data):
        # <applicant> 태그 추가
        self.applicant_tag.text = str(applicant_id)

        # <header> 태그 추가 (결과 코드와 메시지를 포함)
        ET.SubElement(self.header, "resultCode")
        ET.SubElement(self.header, "resultMsg")

        # data 내부에 있는 XML 콘텐츠를 <items>에 추가
        self.__append_items_from_xml_strings(data)
    
    def __done(self):
        # items_elem 초기화
        self.items_elem.clear()
        self.items_elem = ET.SubElement(self.body, "items")
        
    def __get_file_path(self, file_name):
        return f"output/{util.get_timestamp()}/{file_name}.xml"

    def save(self, file_name, applicant_id, data):
        self.__applican_id_regist(applicant_id, data)

        # XML 파일 저장
        file_path = self.__get_file_path(file_name)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        self.tree.write(file_path, encoding="utf-8", xml_declaration=True)

        self.__done()
        print(f"{file_path} 저장 완료")

