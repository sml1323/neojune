
class KiprisFetchData:
    def __init__(self, applicant_id:str, xml_list:list[str]):
        self.applicant_id:str = applicant_id
        self.xml_str_list:list[str] = xml_list