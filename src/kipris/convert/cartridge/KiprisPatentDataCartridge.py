from ...core.convert.KiprisDataCartridge import KiprisDataCartridge
from ....util import util

class KiprisPatentDataCartridge(KiprisDataCartridge):
    def __init__(self):
        super().__init__()


    @property
    def main_ipc(self):
        return util.split(self._main_ipc)
    
    @main_ipc.setter
    def main_ipc(self, value):
        self._main_ipc = value