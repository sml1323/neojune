# XML 저장 함수
from lxml import etree as ET
import os
import logging
def save_data_as_xml(data_dict, file_name, data_type, timestamp):
    valid_count = 0
    root = ET.Element("root")
    folder_path = f"../../res/save_to_xml/{timestamp}"
    os.makedirs(folder_path, exist_ok=True)  # 폴더가 없으면 생성
    # data_dict 순회
    for code, applicants in data_dict.items():
        for applicant_id, data_list in applicants.items():
            for content in data_list:
                # XML 형식인지 확인
                if isinstance(content, str) and content.strip().startswith("<?xml"):
                    try:
                        original_data = ET.fromstring(content.encode("utf-8"))

                        # <data> 요소 생성
                        data_elem = ET.SubElement(root, "data")
                        
                        # <applicantId> 추가
                        applicant_tag = ET.SubElement(data_elem, "applicantId")
                        applicant_tag.text = str(code)
                        
                        # 유형별 태그 추가
                        if "PatentUtilityInfo" in content:
                            items = original_data.find(".//items")
                            if items is not None:
                                for patent_info in items.findall("PatentUtilityInfo"):
                                    data_elem.append(patent_info)
                                    valid_count += 1
                        elif "DesignInfo" in content:
                            items = original_data.find(".//items")
                            if items is not None:
                                for design_info in items.findall("DesignInfo"):
                                    data_elem.append(design_info)
                                    valid_count += 1
                        elif "TradeMarkInfo" in content:
                            items = original_data.find(".//items")
                            if items is not None:
                                for trademark_info in items.findall("TradeMarkInfo"):
                                    data_elem.append(trademark_info)
                                    valid_count += 1
                        else:
                            print(f"{applicant_id}에 유효한 데이터가 없습니다.")
                            
                    except ET.XMLSyntaxError as e:
                        print(f"{applicant_id}의 XML 구문 오류: {e}")
                # XML이 아닌 경우 전체 content를 한 번만 출력
                elif isinstance(content, str):
                    print(f"{data_type}: {applicant_id}의 검색 결과가 XML이 아님: {content}")
                    break  # 한 번만 출력하고 이후 반복 중단

    # XML 파일로 저장
    tree = ET.ElementTree(root)
    file_path = f"../../res/save_to_xml/{file_name}.xml"
    tree.write(file_path, encoding="utf-8", pretty_print=True, xml_declaration=True)
    
    return valid_count