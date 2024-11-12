from ...core.convert.KiprisXmlToDictConverter import KiprisXmlToDictConverter
from ..cartridge.DesignKiprisConvertedDataCartridge import DesignKiprisConvertedDataCartridge
from ..mapper.KiprisDesignXmlMapper import KiprisDesignXmlMapper

class KiprisDesignXmlToDictConverter(KiprisXmlToDictConverter):
    def __init__(self, xml_filename:str=""):
        super().__init__(KiprisDesignXmlMapper(), DesignKiprisConvertedDataCartridge, xml_filename)
        self.item_name = "DesignInfo"