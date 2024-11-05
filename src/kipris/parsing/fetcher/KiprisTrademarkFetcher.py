from ...core.parsing.KiprisFetcher import KiprisFetcher
from ..params.KiprisTrademarkParam import KiprisTrademarkParam

class KiprisTrademarkFetcher(KiprisFetcher):
    def __init__(self, params:list[KiprisTrademarkParam]):
        super().__init__(params=params)
        self.url = "http://plus.kipris.or.kr/openapi/rest/trademarkInfoSearchService/applicantNamesearchInfo"
        self.set_params(params)
        
    def set_params(self, params_list:list[str|int]):
        super().set_params(params_list, KiprisTrademarkParam)
