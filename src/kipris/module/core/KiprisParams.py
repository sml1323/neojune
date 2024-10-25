# import os, sys

# # 현재 파일이 실행되는 경로를 기준으로 설정
# current_dir = os.path.dirname(os.path.abspath(__file__))

# # 실행 경로를 PYTHONPATH에 추가
# sys.path.append(current_dir)


from .KiprisObject import KiprisObject

class KiprisParams(KiprisObject):
    """
    KIPRIS API를 사용하기 위한 파라미터들을 저장하고 관리하는 클래스.

    Attributes:
        ServiceKey (str): API 키.
        applicantName (str): 출원인 이름.
        pageNo (int): 현재 페이지 번호.
        numOfRows (int): 페이지당 표시할 최대 결과 수.

    Methods:
        set_applicantName(applicantName: str): 출원인 이름을 설정합니다.
        set_num_of_rows(value: int): 페이지당 표시할 최대 결과 수를 설정합니다.
    """
    def __init__(self, service_key: str):
        super().__init__()
        self.ServiceKey = service_key  # API 키
        self.applicantName = None  # 출원인 이름
        self.pageNo = 1  # 기본 페이지 번호
        self.numOfRows = 1  # 최대 페이지당 건수
    

    def set_applicantName(self, applicantName: str):
        """출원인 이름을 설정합니다."""
        self.applicantName = applicantName
    
    def set_num_of_rows(self, value: int):
        """페이지당 표시할 최대 결과 수를 설정합니다."""
        self.numOfRows = value

