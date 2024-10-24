from .core.KiprisParams import KiprisParams



class TrademarkParams(KiprisParams):
    def __init__(self, service_key):
        super().__init__(service_key)
        self.freeSearch = None # applicantName가 들어가야함
        self.application ='true'
        self.registration ='true'
        self.refused ='true'
        self.expiration ='true'
        self.withdrawal ='true'
        self.publication ='true'
        self.cancel ='true'
        self.abandonment ='true'
        self.serviceMark = 'true'
        self.trademark ='true'
        self.trademarkServiceMark = 'true'
        self.businessEmblem = 'true'
        self.collectiveMark = 'true'
        self.internationalMark = 'true'
        self.character ='true'
        self.figure ='true'
        self.compositionCharacter ='true'
        self.figureComposition ='true'
        self.sound ='true'
        self.fragrance ='true'
        self.color ='true'
        self.dimension ='true'
        self.colorMixed ='true'
        self.hologram ='true'
        self.motion ='true'
        self.visual ='true'
        self.invisible ='true'
        self.sortSpec ='applicationDate'

    def set_applicantName(self, applicantName: str):
        """
        출원인 명칭으로 검색하기 위해 사용합니다.

        Args:
            applicantName (str): 출원인 명칭
        """
        self.applicantName = applicantName
        self.freeSearch = applicantName
