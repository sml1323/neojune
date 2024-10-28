# utils/logger.py

import logging
import os

def get_logger(name, log_filename="logs/app.log"):
    os.makedirs(os.path.dirname(log_filename), exist_ok=True)
    
    # 로거 설정
    logger = logging.getLogger(name)
    if not logger.hasHandlers():  # 중복 핸들러 방지
        handler = logging.FileHandler(log_filename)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    
    return logger
