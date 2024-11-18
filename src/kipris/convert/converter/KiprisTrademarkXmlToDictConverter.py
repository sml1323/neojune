from ...core.convert.KiprisXmlToDictConverter import KiprisXmlToDictConverter
from ..cartridge.KiprisTrademarkDataCartridge import KiprisTrademarkDataCartridge
from ..mapper.KiprisTrademarkXmlMapper import KiprisTrademarkXmlMapper

class KiprisTrademarkXmlToDictConverter(KiprisXmlToDictConverter):
    def __init__(self, xml_filename:str):
        super().__init__(KiprisTrademarkXmlMapper(), KiprisTrademarkDataCartridge, xml_filename)
        self.item_name = "TradeMarkInfo"
