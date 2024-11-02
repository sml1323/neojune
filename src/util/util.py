import sys
import os
from datetime import datetime

def get_timestamp():
        return datetime.now().strftime("%Y%m%d_%H%M%S")


# 현제 파일 디랙토리 sys path에 추가 함수
def add_sys_path():
    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

