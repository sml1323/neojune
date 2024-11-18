import os
from dotenv import load_dotenv
from ..KiprisObject import KiprisObject
load_dotenv()
service_key = os.getenv('SERVICE_KEY')


class KiprisParam(KiprisObject):
    def __init__(self, app_no=0, applicant_id=0):
        super().__init__()
        self.__app_no = app_no
        self.__applicant_id = applicant_id
        self.accessKey = service_key
        self.docsCount = 500
        self.descSort = 'true'

    @property
    def app_no(self):
        return self.__app_no
    
    @property
    def applicant_id(self):
        return self.__applicant_id