from ...core.prosess.KiprisXmlFileGenerator import KiprisXmlFileGenerator
from ...parsing.fetcher.KiprisTrademarkFetcher import KiprisTrademarkFetcher
from ...core.prosess.enum import KiprisXmlFileGeneratorEntityType

class KiprisTrademarkXmlFileGenerator(KiprisXmlFileGenerator):
    def __init__(self, file_name:str, dir_path:str, applicant_numbers:list[list], entity_type:type[KiprisXmlFileGeneratorEntityType]):
        super().__init__(file_name, dir_path, KiprisTrademarkFetcher, applicant_numbers, entity_type)