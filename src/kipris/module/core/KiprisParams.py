# import os, sys

# # 현재 파일이 실행되는 경로를 기준으로 설정
# current_dir = os.path.dirname(os.path.abspath(__file__))

# # 실행 경로를 PYTHONPATH에 추가
# sys.path.append(current_dir)


from .KiprisObject import KiprisObject

class KiprisParams(KiprisObject):
    def __init__(self, service_key: str):
        super().__init__()
        self.ServiceKey = service_key # api key
        self.applicantName = None # 특허 번호
        self.pageNo = 1  # 기본 페이지 번호
        self.numOfRows = 1  # 최대 페이지당 건수
    
    def prev_page(self):
        self.pageNo -= 1

    def next_page(self):
        self.pageNo += 1
    
    def goto_page(self, page_number: int):
        self.pageNo = page_number

    def set_applicantName(self, applicantName: str):
        self.applicantName = applicantName
    
    def set_num_of_rows(self, value: int):
        self.numOfRows = value

