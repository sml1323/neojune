from ...core.convert.KiprisXmlToDictConverter import KiprisXmlToDictConverter
from ..cartridge.KiprisDesignDataCartridge import KiprisDesignDataCartridge
from ..mapper.KiprisDesignXmlMapper import KiprisDesignXmlMapper

class KiprisDesignXmlToDictConverter(KiprisXmlToDictConverter):
    def __init__(self, xml_filename:str=""):
        super().__init__(KiprisDesignXmlMapper(), KiprisDesignDataCartridge, xml_filename)
        self.item_name = "DesignInfo"