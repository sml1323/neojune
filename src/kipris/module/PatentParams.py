from .core.KiprisParams import KiprisParams


class PatentParams(KiprisParams):
    def __init__(self, service_key):
        super().__init__(service_key)
        self.applicant = None
    
    def set_applicantName(self, applicantName):
        self.applicantName = applicantName
        self.applicant = applicantName
