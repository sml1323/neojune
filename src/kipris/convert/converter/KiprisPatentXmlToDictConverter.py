from ...core.convert.KiprisXmlToDictConverter import KiprisXmlToDictConverter
from ..cartridge.KiprisPatentDataCartridge import KiprisPatentDataCartridge
from ..mapper.KiprisPatentXmlMapper import KiprisPatentXmlMapper

class KiprisPatentXmlToDictConverter(KiprisXmlToDictConverter):
    def __init__(self, xml_filename:str):
        super().__init__(KiprisPatentXmlMapper(), KiprisPatentDataCartridge, xml_filename)
        self.item_name = "PatentUtilityInfo"
