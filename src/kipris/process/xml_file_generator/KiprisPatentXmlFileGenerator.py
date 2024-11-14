from ...core.prosess.KiprisXmlFileGenerator import KiprisXmlFileGenerator
from ...core.prosess.enum import KiprisXmlFileGeneratorEntityType
from ...parsing.fetcher.KiprisPatentFetcher import KiprisPatentFetcher

class KiprisPatentXmlFileGenerator(KiprisXmlFileGenerator):
    def __init__(self, file_name:str, dir_path:str, applicant_numbers:list[list], entity_type:type[KiprisXmlFileGeneratorEntityType]):
        super().__init__(file_name, dir_path, KiprisPatentFetcher, applicant_numbers, entity_type)