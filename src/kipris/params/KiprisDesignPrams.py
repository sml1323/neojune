from ..core.parsing.KiprisParams import KiprisParams

class KiprisDesignPrams(KiprisParams):
    def __init__(self, app_no, applicant_id):
        super().__init__(app_no, applicant_id)
        self.applicantName = app_no
        self.startNumber = 1
        self.etc = 'true'
        self.part = 'true'
        self.simi = 'true'
        self.abandonment = 'true'
        self.cancle = 'true'
        self.destroy = 'true'
        self.invalid = 'true'
        self.notice = 'true'
        self.open = 'true'
        self.registration = 'true'
        self.rejection = 'true'
        self.descSort = 'true'
    
