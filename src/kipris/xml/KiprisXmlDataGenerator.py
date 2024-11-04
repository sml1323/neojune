from .KiprisXmlData import KiprisXmlData
from .KiprisXml import KiprisXml
from ..core.parsing.KiprisFetchData import KiprisFetchData

class KiprisXmlDataGenerator(KiprisXml):
    def __init__(self, data_list:KiprisFetchData|list[KiprisFetchData] = None):
        super().__init__()
        # data_list가 list가 아니면 list로 감싸기
        if not isinstance(data_list, list):
            data_list = [data_list]
            
        self.data_list: list[KiprisXmlData] = []

        # datas가 None이 아니고 첫 번째 요소가 문자열이면 set_kipris_datas 실행
        if data_list and isinstance(data_list[0], KiprisFetchData):
            self.append_data_lists(data_list)

    def append_data_list(self, fetch_data_list: KiprisFetchData):
        xml_data = KiprisXmlData(fetch_data_list)
        xml_data.apply()
        self.data_list.append(xml_data)

    def append_data_lists(self, fetch_data_list:list[KiprisFetchData]):
        for fetch_data in fetch_data_list:
            self.append_data_list(fetch_data)

    def append_data_root(self):
        for data in self.data_list:
            self.root.append(data.root)

    def apply(self):
        self.append_data_root()
    
    def clear(self):
        super().clear()
        self.data_list = []
    
    def save(self, file_name:str, file_path:str=""):
        super().save(file_name, file_path)
        self.clear()