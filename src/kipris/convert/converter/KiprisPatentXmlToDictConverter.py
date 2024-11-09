from typing import List, Dict
from ...core.convert.KiprisXmlToDictConverter import KiprisXmlToDictConverter

class KiprisPatentXmlToDictConverter(KiprisXmlToDictConverter):
    def __init__(self, mapper, xml_filename):
        super().__init__(mapper, xml_filename)
        self.item_name = "PatentUtilityInfo"
