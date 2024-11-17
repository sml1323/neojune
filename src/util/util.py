import os, sys, time, re, json, requests
from datetime import datetime
from functools import wraps, partial
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

def __print_run_time_core(msg:str, end_time, start_time):
    elapsed_time = end_time - start_time
    print("")
    print(f"* {msg}")
    print(f"   - 총 걸린 시간 : {elapsed_time:.2f}초")
    print("")

def execute_with_time(msg:str, callback:callable, *callback_args):
    res = None
    start_time = time.time()
    res = callback(*callback_args)
    end_time = time.time()
    __print_run_time_core(msg, end_time, start_time)
    return res

async def execute_with_time_async(msg:str, callback:callable, *callback_args):
    res = None
    start_time = time.time()
    res = await callback(*callback_args)
    end_time = time.time()
    __print_run_time_core(msg, end_time, start_time)
    return res

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


# def send_slack_message(message):
#     webhook_url = 'https://hooks.slack.com/services/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'
#     headers = {'Content-Type': 'application/json'}
#     data = {'text': message}
    
#     response = requests.post(webhook_url, headers=headers, data=json.dumps(data))
    
#     if response.status_code == 200:
#         print("메시지 전송 성공!")
#     else:
#         print(f"메시지 전송 실패! 상태 코드: {response.status_code}, 응답: {response.text}")


def get_file(file_path):
    with open(file_path, "r") as file:
        return file.read()
    
async def send_slack_message(name, callback:callable, *callback_args):
    def inner(message):
        webhook_url = 'https://hooks.slack.com/services/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'
        headers = {'Content-Type': 'application/json'}
        data = {'text': message}
        
        response = requests.post(webhook_url, headers=headers, data=json.dumps(data))
        
        if response.status_code == 200:
            print("메시지 전송 성공!")
        else:
            print(f"메시지 전송 실패! 상태 코드: {response.status_code}, 응답: {response.text}")
    
    try:
        # partial로 인자를 고정시킨 함수 생성
        inner( f"<!here> 사용 시작 : {name}")
        async_callback = partial(callback, *callback_args)
        await async_callback()
    finally:
        inner( f"<!here> 사용 완료 : {name}")


def execute_sql_files_in_directory(directory: str, prefix: str, mysql):
    """
    지정된 디렉토리에서 특정 접두사(prefix)를 가진 SQL 파일들을 순서대로 실행합니다.
    """
    # 디렉토리에서 해당 prefix로 시작하는 파일만 필터링하고 정렬
    sql_files = []

    for f in os.listdir(directory):
        # 파일 이름이 특정 prefix로 시작하고 .sql로 끝나면 추가
        if f.startswith(prefix) and f.endswith(".sql"):
            sql_files.append(f)

    # 각 파일을 SQL로 실행
    for sql_file in sql_files:
        sql_file_path = os.path.join(directory, sql_file)
        print(sql_file_path)
        mysql.execute_sql_file(sql_file_path)
        print(f"Executed {sql_file_path}")