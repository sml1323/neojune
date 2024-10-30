# TB24_patent
{
  "ipr_seq": "",  # 일련번호 # 
  # applicant_id 이거 추출해서 넣어야함
  "applicant_id": "applicant_id", # 특허고객번호
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
  "pub_num": "PublicNumber",
  "pub_date": "PublicDate",
  "legal_status_desc": "RegistrationStatus",
  "abstract": "Abstract",
  "image_path": "ThumbnailPath",
}

# TB24_design
{
  "ipr_seq": "",
  "applicant_id": "applicant_id",
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
  "pub_num": "publicationNumber",
  "pub_date": "publicationDate",
  "legal_status_desc": "applicationStatus",
  "image_path": "imagePath"
}


# TB24_trademark
{
  "ipr_seq": "",
  "applicant_id": "applicant_id",
  "ipr_code": "ApplicationNumber", # 2 글자
  "title": "Title",
  "serial_no": "SerialNumber",
  "applicant": "ApplicantName",
  "agent": "AgentName",
  "appl_no": "ApplicationNumber",
  "appl_date": "ApplicationDate",
  "pub_num": "PublicNumber",
  "pub_date": "PublicDate",
  "legal_status_desc": "ApplicationStatus",
  "image_path": "ThumbnailPath",
}



# match
{
  'Applicant': "applicant",
  'ApplicationDate': "appl_date",
  'ApplicationNumber': "appl_no, ipr_code: 20",
  'Abstract':  "abstract",
  'DrawingPath': "image_path",
  'SerialNumber': "serial_no",
  'InventionName': "title",
  'OpeningNumber': "open_no",
  'OpeningDate': "open_date",
  'PublicNumber': "pub_num",
  'PublicDate':  "pub_date",
  'RegistrationNumber':  "reg_no",
  'RegistrationDate':  "reg_date",
  'InternationalpatentclassificationNumber': 'A01G 17/12|G09F 7/18|A01G 17/00',
  'RegistrationStatus': "legal_status_desc",
}











