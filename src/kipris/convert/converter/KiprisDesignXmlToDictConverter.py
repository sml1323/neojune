from typing import List, Dict
from ...core.convert.KiprisXmlToDictConverter import KiprisXmlToDictConverter

class KiprisDesignXmlToDictConverter(KiprisXmlToDictConverter):
    def parse(self) -> List[Dict[str, str]]:
        return super().parse("//DesignInfo")  # DesignInfo 요소 찾기