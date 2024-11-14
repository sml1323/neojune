from .KiprisSubProp import KiprisSubProp

class KiprisSubXmlMapper(KiprisSubProp):
    def __init__(self):
        super().__init__()
        self._applicant_id = "applicantId"
        self._appl_no = "appl_no"
        self._serial_no = "serial_no"
