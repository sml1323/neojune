import os
from dotenv import load_dotenv
from ..KiprisObject import KiprisObject

load_dotenv()
service_key = os.getenv('SERVICE_KEY')

class KiprisParamApplicant(KiprisObject):
    def __init__(self, application_no):
        super().__init__()
        self.accessKey = service_key
        self.applicationNumber = application_no

    def set_params(self):
        return super().get_dict_with_properties()