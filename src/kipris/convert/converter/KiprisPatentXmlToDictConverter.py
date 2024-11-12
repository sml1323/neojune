from ...core.convert.KiprisXmlToDictConverter import KiprisXmlToDictConverter
from ..cartridge.PatentKiprisConvertedDataCartridge import PatentKiprisConvertedDataCartridge
from ..mapper.KiprisPatentMapper import KiprisPatentMapper

class KiprisPatentXmlToDictConverter(KiprisXmlToDictConverter):
    def __init__(self, xml_filename:str):
        super().__init__(KiprisPatentMapper(), PatentKiprisConvertedDataCartridge, xml_filename)
        self.item_name = "PatentUtilityInfo"
