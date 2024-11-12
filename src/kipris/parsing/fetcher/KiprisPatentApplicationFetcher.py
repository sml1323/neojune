from ...core.parsing.KiprisFetcher import KiprisFetcher
from ...core.parsing.KiprisParamApplication import KiprisParamApplication

class KiprisPatentParamApplication(KiprisParamApplication):
    def __init__(self, applicationNumber, applicant_id):
        super().__init__(applicationNumber, applicant_id)
        self.patent = 'true'
        self.utility = 'true'
        self.lastvalue = ''
        self.docsStart = 1
        self.app_no = applicationNumber


class KiprisPatentApplicationFetcher(KiprisFetcher):
    def __init__(self, params:list[str|int]):
        super().__init__(params=params)
        self.url = "http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/applicationNumberSearchInfo"
        self.set_params(params)

    def set_params(self, params_list:list[str|int]):
        super().set_params(params_list, KiprisPatentParamApplication)

    