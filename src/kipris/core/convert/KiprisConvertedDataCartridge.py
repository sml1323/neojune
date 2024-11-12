from .KiprisBaseProp import KiprisBaseProp

class KiprisConvertedDataCartridge(KiprisBaseProp):
    def __init__(self):
        super().__init__()
        
    @property
    def ipr_code(self):
        if isinstance(self._ipr_code, str):
            return self._ipr_code[:2]
        else:
            return self._ipr_code
    
    @ipr_code.setter
    def ipr_code(self, value):
        self._ipr_code = value

