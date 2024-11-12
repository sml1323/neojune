from ...core.parsing.KiprisFetcher import KiprisFetcher
from ...core.parsing.KiprisParamApplication import KiprisParamApplication

class KiprisTrademarkParamApplication(KiprisParamApplication):
    def __init__(self, applicationNumber, applicant_id):
        super().__init__(applicationNumber, applicant_id)
        self.application = 'true'
        self.registration = 'true'
        self.refused = 'true'
        self.expiration = 'true'
        self.withdrawal = 'true'
        self.publication = 'true'
        self.cancel = 'true'
        self.abandonment = 'true'
        self.trademark = 'true'
        self.serviceMark = 'true'
        self.trademarkServiceMark = 'true'
        self.businessEmblem = 'true'
        self.collectiveMark = 'true'
        self.geoOrgMark = 'true'
        self.internationalMark = 'true'
        self.certMark = 'true'
        self.geoCertMark = 'true'
        self.character = 'true'
        self.figure = 'true'
        self.compositionCharacter = 'true'
        self.figureComposition = 'true'
        self.sound = 'true'
        self.fragrance = 'true'
        self.color = 'true'
        self.dimension = 'true'
        self.colorMixed = 'true'
        self.hologram = 'true'
        self.motion = 'true'
        self.visual = 'true'
        self.invisible = 'true'
        self.docsStart = 1
        self.app_no = applicationNumber


class KiprisTrademarkApplicationFetcher(KiprisFetcher):
    def __init__(self, params:list[str|int]):
        super().__init__(params=params)
        self.url = "http://plus.kipris.or.kr/openapi/rest/trademarkInfoSearchService/applicationNumberSearchInfo"
        self.set_params(params)

    def set_params(self, params_list:list[str|int]):
        super().set_params(params_list, KiprisTrademarkParamApplication)

    