import os
from lxml import etree

# XML 파일 경로 설정
script_dir = os.path.dirname(os.path.abspath(__file__))
data_file_path = os.path.join(script_dir, 'xml/design_data_20241028_195040.xml')

# 매핑 정보
info = {
  "ipr_seq": "",
  "applicant_no": "",
  "ipr_code": "applicationNumber",  # 2글자
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
}

# 결과 저장을 위한 딕셔너리
result = {}

# XML 데이터 읽기
with open(data_file_path, 'rb') as f:
  xml_string = f.read()
  root = etree.fromstring(xml_string)

  # info 값을 순회하면서 XML 태그에 해당하는 값 추출
  for key, tag_name in info.items():
    if tag_name:  # 태그명이 존재하는 경우에만 추출
      elem = root.xpath(f"//{tag_name}")
      result[key] = elem[0].text if elem else None  # 요소가 있으면 텍스트 추출, 없으면 None
  
  # 결과 출력
  print(result)
