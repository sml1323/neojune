from ...core.convert.KiprisConvertedDataCartridge import KiprisConvertedDataCartridge
from ....util import util

class PatentKiprisConvertedDataCartridge(KiprisConvertedDataCartridge):
    def __init__(self):
        super().__init__()


    @property
    def main_ipc(self):
        return util.split(self._main_ipc)[0]
    
    @main_ipc.setter
    def main_ipc(self, value):
        self._main_ipc = value