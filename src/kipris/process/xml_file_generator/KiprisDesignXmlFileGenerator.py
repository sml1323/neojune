from ...core.prosess.KiprisXmlFileGenerator import KiprisXmlFileGenerator
from ...core.prosess.enum import KiprisXmlFileGeneratorEntityType
from ...parsing.fetcher.KiprisDesignFetcher import KiprisDesignFetcher

class KiprisDesignXmlFileGenerator(KiprisXmlFileGenerator):
    def __init__(self, file_name:str, dir_path:str, applicant_numbers:list[list], entity_type:type[KiprisXmlFileGeneratorEntityType]):
        super().__init__(file_name, dir_path, KiprisDesignFetcher, applicant_numbers, entity_type)