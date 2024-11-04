import os, sys, time
from datetime import datetime

def get_timestamp():
        return datetime.now().strftime("%Y%m%d_%H%M%S")


# 현제 파일 디랙토리 sys path에 추가 함수
def add_sys_path():
    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

async def get_run_time(callback:callable, msg:str):
    start_time = time.time()
    await callback()
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    print(f"총 걸린 시간 : {elapsed_time:.2f}초")
    print(msg)