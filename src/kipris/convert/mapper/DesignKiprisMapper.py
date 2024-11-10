from ...core.convert.KiprisMapper import KiprisMapper

class DesignKiprisMapper(KiprisMapper):
    def __init__(self):
        super().__init__()
        self.ipr_code = "applicationNumber" # 2글자
        self.title = "articleName"
        self.serial_no = "number"
        self.applicant = "applicantName"
        self.appl_no = "applicationNumber"
        self.appl_date = "applicationDate"
        self.pub_num = "publicationNumber"
        self.pub_date = "publicationDate"
        self.legal_status_desc = "applicationStatus"
        self.image_path = "imagePath"

        self.inventor = "inventorName"
        self.agent = "agentName"
        self.open_no = "openNumber"
        self.open_date = "openDate"
        self.reg_no = "registrationNumber"
        self.reg_date = "registrationDate"