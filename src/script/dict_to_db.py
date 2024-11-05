## 예시 데이터 

de = [{
    'ipr_code': '30',
    'title': '지폐계수기',
    "applicant_id": 5576,
    'serial_no': '1',
    'applicant': '주식회사 메카트로',
    'inventor': '고정석|남창우|전재완|정종성',
    'agent': '특허법인주원',
    'appl_no': '3020210019316',
    'appl_date': '20210421',
    'open_no': None,
    'open_date': None,
    'reg_no': '3011244660000',
    'reg_date': '20210818',
    'pub_num': None,
    'pub_date': '20210825',
    'legal_status_desc': '거절',
    'image_path': 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e29e0b68f68d514bb0c87c7ad0d9e286bed75c617e338c490d0b52bbe1949c4f0a7624149d88d6aa0f7de01e5da00cad8310f967ce261403d9'
}]

pa = [{
    'ipr_code': '20',
    'title': '디지탈 날염기',
    "applicant_id":5576,
    'serial_no': '1',
    'applicant': '주식회사 메카트로',
    'main_ipc': 'B41J 3/407',
    'appl_no': '2020020028364',
    'appl_date': '20020919', 
    'open_no': '3011244660000',
    'open_date': '20210818',
    'reg_no': '3011244660000',
    'reg_date': '20210818',
    'pub_num': None,
    'pub_date': None,
    'legal_status_desc': '거절',
    'abstract': '본 고안은 디지털 날염기에 관한 것으로, ... 디지털 날염기를 제공한다. 디지털 날염기, 이송구동수단, 링크결합체, 인쇄감지센서, 자동승강조절수단',
    'image_path': 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e22d01c5c32ba711cfdfd0c8a3560dfe3f5c0c0fb908b6de237d7cc48779f92f863537681dac20830b'
}]


tr = [{
    'ipr_code': '40',
    'title': '(주)메카트로 www.mechatro.co.kr',
    "applicant_id": 5576,
    'serial_no': '1',
    'applicant': '주식회사 메카트로',
    'agent': '신성특허법인(유한)',
    'appl_no': '4020020042375',
    'appl_date': '20020913',
    'pub_num': '4020030051394',
    'pub_date': '20031001',
    'legal_status_desc': '등록',
    'image_path': 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=75a63eed5a438998fe897a23675ce4c3e6785e02ee9396dc96211fb2294abcaac31d9e0c06334f7d7f9f8c59e88e57b7'
}]





############
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from crud.db_crud import upsert_data
from monitoring.prometheus import DB_SAVE_TIME
import time 

# @DB_SAVE_TIME.time()
# def dcit_to_db(table, data : dict):
#     upsert_data(table, data)

def dcit_to_db(table, data: dict):
    # 시작 시간 기록
    start_time = time.time()
    
    # 데이터 저장 작업 수행
    upsert_data(table, data)
    
    # 작업 완료 후 경과 시간 계산 및 관측
    elapsed_time = time.time() - start_time
    DB_SAVE_TIME.labels(table_name=table.split("_")[-1]).observe(elapsed_time)

if __name__ == "__main__":
    dcit_to_db('TB24_patent',pa)
    dcit_to_db('TB24_design',de)
    dcit_to_db('TB24_trademark', tr)