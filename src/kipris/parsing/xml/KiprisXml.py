import os
import lxml.etree as ET
from ....util import util
from ....enum.Config import Config

class KiprisXml:
    def __init__(self):
        self.root = ET.Element("root")

    def __get_file_path(self, file_name, dir_path):
        base_path = Config.OUTPUT_PATH.value
        if dir_path == "":
            return f"{base_path}/{util.get_timestamp()}/{file_name}.xml"
        else:
            return f"{base_path}/{util.get_timestamp()}/{dir_path}/{file_name}.xml"

    
    def xml_to_string(self, xml:ET.Element) -> str:
        return ET.tostring(xml, encoding='utf-8').decode('utf-8')
    
    def save(self, file_name:str, dir_path:str=""):
        dir_path = self.__get_file_path(file_name, dir_path)

        os.makedirs(os.path.dirname(dir_path), exist_ok=True)
        ET.ElementTree(self.root).write(dir_path, encoding="utf-8", xml_declaration=True)
        print(f"{dir_path} 저장 완료")
    
    def clear(self):
        self.root = ET.Element("root")