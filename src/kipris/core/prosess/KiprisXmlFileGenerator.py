from ....enum.KiprisEntityType import KiprisEntityType
from ...core.parsing.KiprisFetcher import KiprisFetcher
from ...parsing.xml.KiprisXmlDataGenerator import KiprisXmlDataGenerator
from ....util import util

class KiprisXmlFileGenerator():
    def __init__(
        self,
        file_name:str, 
        dir_path:str,
        fetcher_class:type[KiprisFetcher],
        applicant_numbers:list[list],
        entity_type:type[KiprisEntityType]
    ):
        self.fetcher:KiprisFetcher = fetcher_class(applicant_numbers)
        self.file_name = file_name
        self.dir_path = dir_path
        self.kipris_xml_dataGenerator = KiprisXmlDataGenerator()
        self.data_list = []
        self.entity_type = entity_type
        
        
    async def __get_xml_data_action(self):
        return await self.fetcher.get_infos(f"{self.file_name}")

    async def __get_xml_data_list(self):
        return await util.execute_with_time_async(f"{self.entity_type.value} {self.file_name} action_api", self.__get_xml_data_action)

    async def __save_action(self, data_list):
        self.kipris_xml_dataGenerator.append_data_lists(data_list)
        self.kipris_xml_dataGenerator.apply()
        self.kipris_xml_dataGenerator.save(self.file_name, self.dir_path)

    async def save(self):
        data_list = await self.__get_xml_data_list()
        await util.execute_with_time_async(f"### {self.entity_type.value} {self.file_name} xml save", self.__save_action, data_list)