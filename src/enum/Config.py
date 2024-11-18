import os
from enum import Enum
from dotenv import load_dotenv
load_dotenv()
class Config(Enum):
    # dev
    OUTPUT_PATH = os.getenv('OUTPUT_PATH')