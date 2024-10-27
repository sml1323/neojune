from ..core.KiprisParams import KiprisParams
from ..core.ServiceNames import ServiceNames


class TrademarkParams(KiprisParams):
    def __init__(self):
        super().__init__(serviceName=ServiceNames.TRADEMARK)
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
