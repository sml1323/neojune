import os
from lxml import etree

script_dir = os.path.dirname(os.path.abspath(__file__))
data_file_path = os.path.join(script_dir, 'xml/design_data_20241028_195040.xml')

with open(data_file_path, 'rb') as f:
    xml_string = f.read()
    root = etree.fromstring(xml_string)
    elem = root.xpath("//applicantName")
    print(elem[0].text)

