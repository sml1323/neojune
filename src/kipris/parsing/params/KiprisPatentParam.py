from ...core.parsing.KiprisParam import KiprisParam

class KiprisPatentParam(KiprisParam):
    def __init__(self, app_no, applicant_id):
        super().__init__(app_no, applicant_id)
        self.applicant = app_no
        self.docsStart = 1
        self.patent = 'true'
        self.utility = 'true'
        self.lastvalue = ''

