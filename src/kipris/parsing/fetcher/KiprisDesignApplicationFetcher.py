from ...core.parsing.KiprisFetcher import KiprisFetcher
from ...core.parsing.KiprisParamApplication import KiprisParamApplication

class KiprisDesignParamApplication(KiprisParamApplication):
    def __init__(self, applicationNumber, applicant_id):
        super().__init__(applicationNumber, applicant_id)
        self.etc = 'true'
        self.part = 'true'
        self.simi = 'true'
        self.abandonment = 'true'
        self.cancle = 'true'
        self.destroy = 'true'
        self.invalid = 'true'
        self.notice = 'true'
        self.open = 'true'
        self.registration = 'true'
        self.rejection = 'true'
        self.startNumber = 1
        self.app_no = applicationNumber


class KiprisDesignApplicationFetcher(KiprisFetcher):
    def __init__(self, params:list[str|int]):
        super().__init__(params=params)
        self.url = "http://plus.kipris.or.kr/openapi/rest/designInfoSearchService/applicationNumberSearchInfo"
        self.set_params(params)

    def set_params(self, params_list:list[str|int]):
        super().set_params(params_list, KiprisDesignParamApplication)

    