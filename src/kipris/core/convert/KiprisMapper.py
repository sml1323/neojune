from ..KiprisObject import KiprisObject

class KiprisMapper(KiprisObject):
    def __init__(self):
        super().__init__()
        self.ipr_seq = None
        self.applicant_id = None
        # 분리
        self.ipr_code = None
        self.title = None
        self.serial_no = None
        self.applicant = None
        self.appl_no = None
        self.appl_date = None
        self.pub_num = None
        self.pub_date = None
        self.legal_status_desc = None
        self.image_path = None