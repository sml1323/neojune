from .KiprisMapper import KiprisMapper

class KiprisConvertedDataCartridge(KiprisMapper):
    def __init__(self):
        super().__init__()
        
    @property
    def ipr_code(self):
        return self._ipr_code[:2]
    
    @ipr_code.setter
    def ipr_code(self, value):
        self._ipr_code = value

