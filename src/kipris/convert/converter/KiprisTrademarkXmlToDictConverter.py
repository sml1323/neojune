from ...core.convert.KiprisXmlToDictConverter import KiprisXmlToDictConverter
from ..cartridge.TrademarkKiprisConvertedDataCartridge import TrademarkKiprisConvertedDataCartridge
from ..mapper.KiprisTrademarkMapper import KiprisTrademarkMapper

class KiprisTrademarkXmlToDictConverter(KiprisXmlToDictConverter):
    def __init__(self, xml_filename:str):
        super().__init__(KiprisTrademarkMapper(), TrademarkKiprisConvertedDataCartridge, xml_filename)
        self.item_name = "TradeMarkInfo"
