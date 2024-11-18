import os, logging
from ..util import util # 와.. 사람 잡네 이거.. 같은 디렉토리인데 왜 .. 임? 와..... 진짜 너무하다..
from ..enum.KiprisEntityType import KiprisEntityType
from ..enum.ApiType import ApiType
from ..enum.TableName import TableName

def __setup_logger_core(name, file_handler):
    # service
    dir_path = f'/app/res/output/{util.get_timestamp()}/log'

    # dev
    # dir_path = f'{util.add_sys_path()}/res/log/'
    os.makedirs(dir_path, exist_ok=True)
    pass
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # 파일 핸들러
        os.makedirs(os.path.dirname(dir_path), exist_ok=True)
        fh = logging.FileHandler(f'{dir_path}/{file_handler}')
        fh.setLevel(logging.DEBUG)  # INFO 레벨로 변경
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    return logger

def setup_logger(name):
    return __setup_logger_core(name, f"{util.get_timestamp()}_api.log")

def setup_logger_origin(name):
    return __setup_logger_core(name, "origin.log")

def setup_bin_logger(table_name:TableName, entity_type:KiprisEntityType, api_type:ApiType):
    logger = setup_logger(f'{entity_type.value}: {api_type.value}')
    logger.debug(table_name.value)
