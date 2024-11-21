#!/bin/bash
### save_to_xml company_patent
python main.py save_to_xml company_patent
python main.py save_to_xml company_design
python main.py save_to_xml company_trademark
python main.py save_to_xml university_patent
python main.py save_to_xml university_design
python main.py save_to_xml university_trademark

### xml_to_sql company_patent
python main.py xml_to_sql company_patent
python main.py xml_to_sql company_design
python main.py xml_to_sql company_trademark
python main.py xml_to_sql university_patent
python main.py xml_to_sql university_design
python main.py xml_to_sql university_trademark

### sql_to_db base
python main.py sql_to_db base company_patent
python main.py sql_to_db base company_design
python main.py sql_to_db base company_trademark
python main.py sql_to_db base university_patent
python main.py sql_to_db base university_design
python main.py sql_to_db base university_trademark

### sql_to_db ipc_cpc
python main.py sql_to_db ipc_cpc company_patent
python main.py sql_to_db ipc_cpc university_patent # err

### sql_to_db priority
python main.py sql_to_db priority company_design
python main.py sql_to_db priority company_trademark
python main.py sql_to_db priority university_design
python main.py sql_to_db priority university_trademark