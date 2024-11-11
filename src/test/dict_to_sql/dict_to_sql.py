# from ....kipris.upload.uploader.KiprisTB24DesignDataUploader import KiprisTB24DesignDataUploader

data = [
    {
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

def get_dict_to_tuples(data:dict):
        # [] 말고 (),() 식으로 만들기 
    res = []
    for d in data:
        values = tuple(d.values())  # 딕셔너리 d의 값을 튜플로 변환
        res.append(values)  # 변환된 튜플을 리스트에 추가
    return res
    # 여기서 정제할것( title , appl_no 이 None값인거 제외) 
# KiprisTB24DesignDataUploader().upload(design)



## mysql.py에 있는 내용들 
table_name = 'TB24_company_design'
columns = data[0].keys()
placeholders = ', '.join(['%s'] * len(columns))


        
additional_update_clause = """
reg_no = VALUES(reg_no),
reg_date = VALUES(reg_date),
open_no = VALUES(open_no),
open_date = VALUES(open_date),
""" if table_name in ["TB24_company_design", "TB2_patent"] else ""

common_update_clause = """
legal_status_desc = VALUES(legal_status_desc),
pub_num = VALUES(pub_num),
pub_date = VALUES(pub_date)
"""

sql = f"""
INSERT INTO {table_name} ({', '.join(columns)}) 
VALUES ({get_dict_to_tuples(data)})
ON DUPLICATE KEY UPDATE
{additional_update_clause}
{common_update_clause};
"""
#  file out
# sql = f"""
#     INSERT INTO {table_name} ({', '.join(columns)}) 
#     VALUES ({placeholders})
#     ON DUPLICATE KEY UPDATE
#     {additional_update_clause}
#     {common_update_clause};
# """

'''
INSERT INTO TB24_company_design (agent, appl_date, appl_no, applicant, applicant_id, image_path, inventor, ipr_code, legal_status_desc, open_date, open_no, pub_date, pub_num, reg_date, reg_no, serial_no, title) VALUES 
('최경수', '20140408', '3020140017534', '주식회사 파인메딕스|전성우', 2, 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e29e0b68f68d514bb0fedbb1325566a2d358de5f2bd287de10331b3d1887947c482a970947ddae1bf2bf9cda621bd8ba0d7223906319bd9903', '전성우', '30', '등록', None, None, '20141205', None, '20141201', '3007743290000', '1', '내시경시술용 핸들')

ON DUPLICATE KEY UPDATE
reg_no = VALUES(reg_no),
reg_date = VALUES(reg_date),
open_no = VALUES(open_no),
open_date = VALUES(open_date),
legal_status_desc = VALUES(legal_status_desc),
pub_num = VALUES(pub_num),
pub_date = VALUES(pub_date);
'''

def main():
    print(sql)
    pass