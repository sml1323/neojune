from ...core.parsing.KiprisParam import KiprisParam


class KiprisTrademarkParam(KiprisParam):
    def __init__(self, app_no, applicant_id):
        super().__init__(app_no, applicant_id)
        self.applicantName = app_no
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