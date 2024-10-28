import os, xmltodict

# lxml 혹은? xmltodict를 사용할지 라이브러리

script_dir = os.path.dirname(os.path.abspath(__file__))
data_file_path = os.path.join(script_dir, '1.patent.xml')

with open(data_file_path, 'r', encoding='utf-8') as f:
    xml_string = f.read()
    # print(xml_string)
    print(xmltodict.parse(xml_string))



# # data.xml 불러오기
# with open('./data.xml', 'r', encoding='utf-8') as f:
#     # print(f)
#     xmlString = f.read()
#     # print(xmlString)
    
#     xmltodict.parse(xmlString)
