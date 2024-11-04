from ...core.convert.KiprisMapping import KiprisMapping

class PatentKiprisMapping(KiprisMapping):
    def __init__(self):
        super().__init__()
        self.ipr_code = "ApplicationNumber"
        self.title = "InventionName"
        self.serial_no = "SerialNumber"
        self.applicant = "Applicant"
        self.appl_no = "ApplicationNumber"
        self.appl_date = "ApplicationDate"
        self.pub_num = "PublicNumber"
        self.pub_date = "PublicDate"
        self.legal_status_desc = "RegistrationStatus"
        self.image_path = "ThumbnailPath"

        self.reg_no = "RegistrationNumber"
        self.reg_date = "RegistrationDate"
        self.open_no = "OpeningNumber"
        self.open_date = "OpeningDate"
        self.main_ipc = "InternationalpatentclassificationNumber"
        self.abstract = "Abstract"