import os
from dotenv import load_dotenv
from ..KiprisObject import KiprisObject
from ....util.util import get_timestamp
load_dotenv()
service_key = os.getenv('SERVICE_KEY')

class KiprisParamChange(KiprisObject):
    def __init__(self):
        super().__init__()
        self.ServiceKey = service_key
        self.date = get_timestamp()

    def set_params(self):
        return super().get_dict_with_properties()
