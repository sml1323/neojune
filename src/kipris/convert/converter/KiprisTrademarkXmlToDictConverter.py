from typing import List, Dict
from ...core.convert.KiprisXmlToDictConverter import KiprisXmlToDictConverter

class KiprisTrademarkXmlToDictConverter(KiprisXmlToDictConverter):
    def parse(self) -> List[Dict[str, str]]:
        return super().parse("//TradeMarkInfo")  # TradeMarkInfo 요소 찾기
