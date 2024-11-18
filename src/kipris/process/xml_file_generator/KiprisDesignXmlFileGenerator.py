from ...core.prosess.KiprisXmlFileGenerator import KiprisXmlFileGenerator
from ....enum.KiprisEntityType import KiprisEntityType
from ...parsing.fetcher.KiprisDesignFetcher import KiprisDesignFetcher

class KiprisDesignXmlFileGenerator(KiprisXmlFileGenerator):
    def __init__(self, file_name:str, dir_path:str, applicant_numbers:list[list], entity_type:type[KiprisEntityType]):
        super().__init__(file_name, dir_path, KiprisDesignFetcher, applicant_numbers, entity_type)