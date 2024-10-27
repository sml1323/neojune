import os

from .KiprisObject import KiprisObject
from .ServiceNames import ServiceNames


service_key = os.getenv('SERVICE_KEY')


class KiprisParams(KiprisObject):
    """
    KIPRIS API를 사용하기 위한 파라미터들을 저장하고 관리하는 클래스.

    Attributes:
        ServiceKey (str): API 키.
        applicantName (str): 특허번호.
        pageNo (int): 현재 페이지 번호.
        numOfRows (int): 페이지당 표시할 최대 결과 수.

    Methods:
        set_applicantName(applicantName: str): 특허번호를 설정합니다.
        set_num_of_rows(value: int): 페이지당 표시할 최대 결과 수를 설정합니다.
    """
    def __init__(self, serviceName:ServiceNames):
        super().__init__()
        self.ServiceKey = service_key  # API 키
        self.applicantName = None  # 특허번호
        self.applicant = None # 특허번호
        self.freeSearch = None # 특허번호
        self.pageNo = 1  # 기본 페이지 번호
        self.numOfRows = 1  # 최대 페이지당 건수
        self.serviceName = serviceName.value
    

    def set_applicantName(self, applicantName: str):
        """특허번호를 설정합니다."""
        self.applicantName = applicantName
    
    def set_num_of_rows(self, value: int):
        """페이지당 표시할 최대 결과 수를 설정합니다."""
        self.numOfRows = value

