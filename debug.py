import asyncio
from src.test import test
from src.bin import save_to_xml, xml_to_sql, sql_to_db



test.run()

# asyncio.run(save_to_xml.run_company_design())
# asyncio.run(save_to_xml.run_company_patent())
# asyncio.run(save_to_xml.run_company_trademark())
# asyncio.run(save_to_xml.run_university_design())
# asyncio.run(save_to_xml.run_university_patent())
# asyncio.run(save_to_xml.run_university_trademark())

# xml_to_sql.run_company_design()
# xml_to_sql.run_company_patent()
# xml_to_sql.run_company_trademark()
# xml_to_sql.run_university_design()
# xml_to_sql.run_university_patent()
# xml_to_sql.run_university_trademark()


# sql_to_db.run_company_design()
# sql_to_db.run_company_patent()
# sql_to_db.run_company_trademark()
# sql_to_db.run_university_design()
# sql_to_db.run_university_patent()
# sql_to_db.run_university_trademark()