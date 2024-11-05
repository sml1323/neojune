import os, sys, time, re
from datetime import datetime

def get_timestamp():
    return datetime.now().strftime("%Y%m%d")


# 현제 파일 디랙토리 sys path에 추가 함수
def add_sys_path():
    # sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    return root_dir

async def get_run_time(callback:callable, msg:str):
    start_time = time.time()
    await callback()
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    print(f"총 걸린 시간 : {elapsed_time:.2f}초")
    print(msg)

def clean_whitespace(text: str) -> str:
    """텍스트의 여러 개 공백을 하나로 줄이고, 앞뒤 공백을 제거."""
    return re.sub(r'\s+', ' ', text).strip()

def split(text: str, seperator: str = '|') -> str:
    return text.split(seperator)
