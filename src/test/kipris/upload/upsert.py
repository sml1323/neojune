# from ....kipris.upload.uploader.KiprisTB24DesignDataUploader import KiprisTB24DesignDataUploader

data = [{
    'agent': '최경수',
    'appl_date': '20140408',
    'appl_no': '3020140017534',
    'applicant': '주식회사 파인메딕스|전성우',
    'applicant_id': 2,
    'image_path': 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e29e0b68f68d514bb0fedbb1325566a2d358de5f2bd287de10331b3d1887947c482a970947ddae1bf2bf9cda621bd8ba0d7223906319bd9903',
    'inventor': '전성우',
    'ipr_code': '30',
    # 'ipr_seq': '',
    'legal_status_desc': '등록',
    'open_date': None,
    'open_no': None,
    'pub_date': '20141205',
    'pub_num': None,
    'reg_date': '20141201',
    'reg_no': '3007743290000',
    'serial_no': '1',
    'title': '내시경시술용 핸들'
},
]

# KiprisTB24DesignDataUploader().upload(design)

## mysql.py에 있는 내용들 
table_name = 'TB24_company_design'
columns = data[0].keys()
placeholders = ', '.join(['%s'] * len(columns))

common_update_clause = """
    legal_status_desc = VALUES(legal_status_desc),
    pub_num = VALUES(pub_num),
    pub_date = VALUES(pub_date)
"""
        
additional_update_clause = """
    reg_no = VALUES(reg_no),
    reg_date = VALUES(reg_date),
    open_no = VALUES(open_no),
    open_date = VALUES(open_date),
""" if table_name in ["TB24_company_design", "TB2_patent"] else ""

# sql = f"""
#     INSERT INTO {table_name} ({', '.join(columns)}) 
#     VALUES ({placeholders})
#     ON DUPLICATE KEY UPDATE
#     {additional_update_clause}
#     {common_update_clause};
# """

# [] 말고 (),() 식으로 만들기 
data_values = [tuple(d.values()) for d in data]
# 여기서 정제할것( title , appl_no 이 None값인거 제외) 
sql = f"""
    INSERT INTO {table_name} ({', '.join(columns)}) 
    VALUES ({data_values})
    ON DUPLICATE KEY UPDATE
    {additional_update_clause}
    {common_update_clause};
"""

print(sql)
#  file out
