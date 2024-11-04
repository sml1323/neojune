from ..core.parsing.KiprisFetcher import KiprisFetcher
from ..params.KiprisPatentParams import KiprisPatentParams

class KiprisPatentFetcher(KiprisFetcher):
    def __init__(self, params:list[KiprisPatentParams]):
        super().__init__(params=params)
        self.url = "http://plus.kipris.or.kr/openapi/rest/patUtiModInfoSearchSevice/applicantNameSearchInfo"
        self.set_params(params)

    
    def set_params(self, params_list:list[str|int]):
        super().set_params(params_list, KiprisPatentParams)