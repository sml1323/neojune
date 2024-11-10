from ...core.convert.KiprisXmlToDictConverter import KiprisXmlToDictConverter
from ..cartridge.PatentKiprisConvertedDataCartridge import PatentKiprisConvertedDataCartridge

class KiprisPatentXmlToDictConverter(KiprisXmlToDictConverter):
    def __init__(self, mapper, xml_filename):
        super().__init__(mapper, PatentKiprisConvertedDataCartridge, xml_filename)
        self.item_name = "PatentUtilityInfo"
