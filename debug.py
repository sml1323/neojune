import asyncio
from src.test import test
from src.bin import save_to_xml, xml_to_sql, dict_to_sql_sub
from src.bin.sql_to_db import base, ipc_cpc, priority

# 개발용 
# test.run() 

# 하나씩 돌려야 돌아감
# asyncio.run(save_to_xml.run_company_design())
# asyncio.run(save_to_xml.run_company_patent())
# asyncio.run(save_to_xml.run_company_trademark())
# asyncio.run(save_to_xml.run_university_design())
# asyncio.run(save_to_xml.run_university_patent())
# asyncio.run(save_to_xml.run_university_trademark())

xml_to_sql.run_company_design()
xml_to_sql.run_company_patent()
xml_to_sql.run_company_trademark()
xml_to_sql.run_university_design()
xml_to_sql.run_university_patent()
xml_to_sql.run_university_trademark()

base.run_company_design()
base.run_company_patent()
base.run_company_trademark()
base.run_university_design()
base.run_university_patent()
base.run_university_trademark()

dict_to_sql_sub.run_company_design()
dict_to_sql_sub.run_company_patent()
dict_to_sql_sub.run_company_trademark()
dict_to_sql_sub.run_university_design()
dict_to_sql_sub.run_university_patent()
dict_to_sql_sub.run_university_trademark()

priority.run_company_design()
ipc_cpc.run_company_patent()
priority.run_company_trademark() 
priority.run_university_design()
ipc_cpc.run_university_patent()
priority.run_university_trademark()