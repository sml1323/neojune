import os
import lxml.etree as ET
from ....util import util

class KiprisXml:
    def __init__(self):
        self.root = ET.Element("root")

    def __get_file_path(self, file_name):
        return f"output/{util.get_timestamp()}/{file_name}.xml"
    
    def xml_to_string(self, xml:ET.Element) -> str:
        return ET.tostring(xml, encoding='utf-8').decode('utf-8')
    
    def save(self, file_name:str, file_path:str=""):
        if file_path == "":
            file_path = self.__get_file_path(file_name)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        ET.ElementTree(self.root).write(file_path, encoding="utf-8", xml_declaration=True)
        print(f"{file_path} 저장 완료")
    
    def clear(self):
        self.root = ET.Element("root")