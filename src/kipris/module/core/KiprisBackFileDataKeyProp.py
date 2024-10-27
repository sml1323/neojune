from .KiprisObject import KiprisObject

class KiprisBackFileDataKeyProp(KiprisObject):
    def __init__(self):
        super().__init__()
        self.index = None # 인덱스 또는 번호
        self.title = None # 발명의 제목 또는 상품의 명칭
        self.drawing = None # 도면 또는 이미지 경로
        self.legal_status_desc = None # 법적 상태 설명
        self.ipr_code = None  # 지식재산권 코드
        self.applicant = 'applicationName' # 법인번호
        self.inventor = 'inventorname' # 발명자
        self.agent = 'agentName' # 대리인
        self.appl_no = 'applicationNumber' # 출원 번호
        self.appl_date = 'applicationDate' # 출원 일자
        self.open_no = 'openNumber' # 공개 번호
        self.open_date = 'openDate' # 공개 일자
        self.reg_no = 'registerNumber' # 등록 번호
        self.reg_date = 'registerDate' # 등록 일자
        self.pub_no = 'publicationNumber' # 공고 번호
        self.pub_date = 'publicationDate' # 공고 일자
        self.ipc_number = 'ipcNumber' # 국제 특허 분류
