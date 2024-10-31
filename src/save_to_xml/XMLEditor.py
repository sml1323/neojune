import os
import xml.etree.ElementTree as ET
from ..util import util



class XMLEditor:
    def __init__(self):
        pass

    def save_data_as_xml(self, applicant_id, data, file_name):
        # XML 루트 요소 생성
        root = ET.Element("responseData")
        response_elem = ET.SubElement(root, "response")

        # <applicant> 태그 추가
        applicant_tag = ET.SubElement(response_elem, "applicant_id")
        applicant_tag.text = str(applicant_id)

        # <header> 태그 추가 (결과 코드와 메시지를 포함)
        header = ET.SubElement(response_elem, "header")
        ET.SubElement(header, "resultCode")
        ET.SubElement(header, "resultMsg")

        # <body> 태그 추가 및 그 안에 <items> 데이터 삽입
        body = ET.SubElement(response_elem, "body")
        items_elem = ET.SubElement(body, "items")

        # data 내부에 있는 XML 콘텐츠를 <items>에 추가
        for content in data:
            original_data = ET.fromstring(content)

            # 기존 XML에서 <items> 내부 태그들만 추가
            items = original_data.find(".//items")
            if items is not None:
                for elem in items:
                    items_elem.append(elem)

        # XML 파일 저장
        file_path = f"output/{util.get_timestamp()}/{file_name}.xml"
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        tree = ET.ElementTree(root)
        tree.write(file_path, encoding="utf-8", xml_declaration=True)
        print(f"{file_path} 저장 완료")

