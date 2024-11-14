from .KiprisSubProp import KiprisSubProp

class KiprisXmlMapper(KiprisSubProp):
    def __init__(self):
        super().__init__()
        self.applicant_id = "applicantId"
        self.appl_no = "appl_no"
        self.serial_no = "serial_no"
