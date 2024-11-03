from ..core.KiprisParams import KiprisParams

class PatentParams(KiprisParams):
    def __init__(self, applicant):
        super().__init__()
        self.applicant = applicant
        self.docsStart = 1
        self.patent = 'true'
        self.utility = 'true'
        self.lastvalue = ''

