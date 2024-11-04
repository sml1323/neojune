import os
import lxml.etree as ET
from ..core.KiprisFetchData import KiprisFetchData
from .KiprisXml import KiprisXml


class KiprisXmlData(KiprisXml):
    def __init__(self, data:KiprisFetchData):
        super().__init__()
        self.root = self.__get_base_xml()
        self.data:KiprisFetchData = data

    def __get_base_xml(self):
        base_path = os.path.dirname(__file__)
        return ET.parse(f"{base_path}/kipris_base.xml").getroot()

    def fromstring(self, xml_str):
        return ET.fromstring(xml_str.encode('utf-8'))
    
    def get_item_group_elem(self) ->ET.Element:
        return self.root.find("itemGrop")
    
    def get_appli_id_elem(self) ->ET.Element:
        return self.root.find("applicantId")
    
    def append_applicant_id(self):
        applicant_id = self.get_appli_id_elem()
        applicant_id.text = str(self.data.applicant_id)

    def append_items(self):
        item_group = self.get_item_group_elem()
        for xml_str in self.data.xml_str_list:
            item_group.append(self.fromstring(xml_str).find('body/items'))


    def get_merge_item_elem(self, xml_string:list[str]) -> list[ET.Element]:
        res_items = ET.Element("items")

        for xml in xml_string:
            items = ET.fromstring(xml).find("body/items")
            for item in items:
                res_items.append(item)
        return res_items


    def apply(self):
        self.append_applicant_id()
        self.append_items()


