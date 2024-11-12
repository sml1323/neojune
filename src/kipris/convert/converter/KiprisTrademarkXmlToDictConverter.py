from ...core.convert.KiprisXmlToDictConverter import KiprisXmlToDictConverter
from ..cartridge.TrademarkKiprisConvertedDataCartridge import TrademarkKiprisConvertedDataCartridge
from ..mapper.KiprisTrademarkXmlMapper import KiprisTrademarkXmlMapper

class KiprisTrademarkXmlToDictConverter(KiprisXmlToDictConverter):
    def __init__(self, xml_filename:str):
        super().__init__(KiprisTrademarkXmlMapper(), TrademarkKiprisConvertedDataCartridge, xml_filename)
        self.item_name = "TradeMarkInfo"
