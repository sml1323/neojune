import os
from dotenv import load_dotenv
from ..KiprisObject import KiprisObject
load_dotenv()
service_key = os.getenv('SERVICE_KEY')


class KiprisParamApplication(KiprisObject):
    def __init__(self, applicationNumber, applicant_id):
        super().__init__()
        self.accessKey = service_key
        self.docsCount = 500
        self.applicationNumber = applicationNumber
        self.applicant_id = applicant_id