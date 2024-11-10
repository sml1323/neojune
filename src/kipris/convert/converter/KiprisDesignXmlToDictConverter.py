from ...core.convert.KiprisXmlToDictConverter import KiprisXmlToDictConverter
from ..cartridge.DesignKiprisConvertedDataCartridge import DesignKiprisConvertedDataCartridge

class KiprisDesignXmlToDictConverter(KiprisXmlToDictConverter):
    def __init__(self, mapper, xml_filename):
        super().__init__(mapper, DesignKiprisConvertedDataCartridge, xml_filename)
        self.item_name = "DesignInfo"