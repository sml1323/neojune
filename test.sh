#!/bin/bash

python main.py --run save_to_xml company_patent
python main.py --run save_to_xml company_design
python main.py --run save_to_xml company_trademark
python main.py --run save_to_xml university_patent
python main.py --run save_to_xml university_design
python main.py --run save_to_xml university_trademark


python main.py --run xml_to_sql company_patent
python main.py --run xml_to_sql company_design
python main.py --run xml_to_sql company_trademark
python main.py --run xml_to_sql university_patent
python main.py --run xml_to_sql university_design
python main.py --run xml_to_sql university_trademark