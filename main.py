import asyncio

from src.script import dict_to_db, save_to_xml , xml_to_dict
from prometheus_client import  start_http_server


start_http_server(8080)

# asyncio.run(save_to_xml.main())


import time
start = time.time()
design_results,  patent_results, trademark_results = xml_to_dict.main()
print("data parsing" , time.time() - start)



start = time.time()
if patent_results:
   dict_to_db.dcit_to_db('TB24_patent',patent_results)
print("patent " , time.time() - start)
start = time.time()
if patent_results:
    dict_to_db.dcit_to_db('TB24_design',design_results)
print("design" ,time.time() - start)
start = time.time()
if trademark_results:
    dict_to_db.dcit_to_db('TB24_trademark', trademark_results)
print("trademark" , time.time() - start)