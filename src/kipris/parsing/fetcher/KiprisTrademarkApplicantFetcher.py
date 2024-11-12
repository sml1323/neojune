import os
from dotenv import load_dotenv
from ...core.parsing.KiprisParamApplicant import KiprisParamApplicant
from ...core.parsing.KiprisApplicantFetcher import KiprisApplicantFetcher
from ....util.util import get_timestamp
load_dotenv()
service_key = os.getenv('SERVICE_KEY')

class KiprisTrademarkApplicantFetcher(KiprisApplicantFetcher):
    def __init__(self, applicationNumber_list : list[str]):
        super().__init__(params=applicationNumber_list)
        self.url = "http://plus.kipris.or.kr/openapi/rest/trademarkInfoSearchService/trademarkApplicantInfo"
        self.set_params(applicationNumber_list)

    def set_params(self, applicationNumber_list : list[str]):
        super().set_params(applicationNumber_list, KiprisParamApplicant)

