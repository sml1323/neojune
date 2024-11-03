import os

from .KiprisObject import KiprisObject


service_key = os.getenv('SERVICE_KEY')


class KiprisParams(KiprisObject):
    def __init__(self):
        super().__init__()
        self.accessKey = service_key
        self.docsCount = 500

