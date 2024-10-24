from .core.KiprisParams import KiprisParams


class PatentParams(KiprisParams):
    def __init__(self, service_key):
        super().__init__(service_key)
        self.applicant = None
    
    def set_applicantName(self, applicantName):
        """특허 출원인 명칭을 설정합니다.

        Args:
            applicantName (str): 특허 출원인 명칭
        """
        self.applicantName = applicantName
        self.applicant = applicantName
