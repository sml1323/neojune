from ...core.convert.KiprisXmlToDictConverter import KiprisXmlToDictConverter
from ..cartridge.TrademarkKiprisConvertedDataCartridge import TrademarkKiprisConvertedDataCartridge

class KiprisTrademarkXmlToDictConverter(KiprisXmlToDictConverter):
    def __init__(self, mapper, xml_filename):
        super().__init__(mapper, TrademarkKiprisConvertedDataCartridge, xml_filename)
        self.item_name = "TradeMarkInfo"
