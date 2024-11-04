import logging

def setup_logger(name):
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # 파일 핸들러
        fh = logging.FileHandler('api.log')
        fh.setLevel(logging.DEBUG)  # INFO 레벨로 변경
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    
    return logger

def setup_logger_db(name):
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # 파일 핸들러
        fh = logging.FileHandler('db.log')
        fh.setLevel(logging.DEBUG)  # INFO 레벨로 변경
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    
    return logger