import os, sys, time, re
from datetime import datetime
from functools import wraps
import contextlib
import asyncio
import yappi
import requests
import json

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
    print(f"총 걸린 시간 : {elapsed_time:.2f}초, {msg}")

def clean_whitespace(text: str) -> str:
    """텍스트의 여러 개 공백을 하나로 줄이고, 앞뒤 공백을 제거."""
    return re.sub(r'\s+', ' ', text).strip()

def split(text: str, seperator: str = '|') -> str:
    return text.split(seperator)



#         return sync_wrapper
def yappi_profiler(file_name="callgrind"):  # 기본 파일 이름 설정
    def decorator(func):
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            yappi.set_clock_type("WALL")
            yappi.start()
            try:
                return await func(*args, **kwargs)
            finally:
                yappi.stop()
                # 프로파일 결과를 지정된 파일로 저장
                yappi.get_func_stats().save(f"{file_name}.prof", "pstat")
    
        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            yappi.set_clock_type("WALL")
            yappi.start()
            try:
                return func(*args, **kwargs)
            finally:
                yappi.stop()
                # 프로파일 결과를 지정된 파일로 저장
                yappi.get_func_stats().save(f"{file_name}.prof", "pstat")
        
        # 비동기 함수인지 확인하여 적절한 래퍼 사용
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        else:
            return sync_wrapper

    return decorator


def send_slack_message( message):
    webhook_url = 'https://hooks.slack.com/services/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'
    headers = {'Content-Type': 'application/json'}
    data = {'text': message}
    
    response = requests.post(webhook_url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        print("메시지 전송 성공!")
    else:
        print(f"메시지 전송 실패! 상태 코드: {response.status_code}, 응답: {response.text}")
