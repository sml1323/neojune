import os, logging
from ..util import util # 와.. 사람 잡네 이거.. 같은 디렉토리인데 왜 .. 임? 와..... 진짜 너무하다..


def __setup_logger_core(name, file_handler):
    dir_path = f'{util.add_sys_path()}/res/log/'
    os.makedirs(os.path.dirname(dir_path), exist_ok=True)
    pass
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # 파일 핸들러
        os.makedirs(os.path.dirname(dir_path), exist_ok=True)
        fh = logging.FileHandler(f'res/log/{file_handler}')
        fh.setLevel(logging.DEBUG)  # INFO 레벨로 변경
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    return logger

def setup_logger(name):
    return __setup_logger_core(name, "api.log")

def setup_logger_origin(name):
    return __setup_logger_core(name, "origin.log")
