from ..core.KiprisParams import KiprisParams


class KiprisTrademarkParams(KiprisParams):
    def __init__(self, applicant):
        super().__init__()
        self.applicantName = applicant
        self.docsStart = 1
        self.abandonment = 'true'
        self.application = 'true'
        self.cancel = 'true'
        self.expiration = 'true'
        self.publication = 'true'
        self.refused = 'true'
        self.registration = 'true'
        self.withdrawal = 'true'
        self.businessEmblem = 'true'
        self.certMark = 'true'
        self.collectiveMark = 'true'
        self.geoCertMark = 'true'
        self.geoOrgMark = 'true'
        self.internationalMark = 'true'
        self.serviceMark = 'true'
        self.trademark = 'true'
        self.trademarkServiceMark = 'true'
        self.character = 'true'
        self.compositionCharacter = 'true'
        self.figure = 'true'
        self.figureComposition = 'true'
        self.fragrance = 'true'
        self.sound = 'true'
        self.color = 'true'
        self.colorMixed = 'true'
        self.dimension = 'true'
        self.hologram = 'true'
        self.invisible = 'true'
        self.motion = 'true'
        self.visual = 'true'
        self.descSort = 'true'
