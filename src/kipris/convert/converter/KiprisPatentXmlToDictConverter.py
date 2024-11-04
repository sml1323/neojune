from typing import List, Dict
from ...core.convert.KiprisXmlToDictConverter import KiprisXmlToDictConverter

class KiprisPatentXmlToDictConverter(KiprisXmlToDictConverter):
    def parse(self) -> List[Dict[str, str]]:
        return super().parse("//PatentUtilityInfo")  # PatentUtilityInfo 요소 찾기
