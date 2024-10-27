from ..core.KiprisBackFileDataKeyProp import KiprisBackFileDataKeyProp

class TrademarkBackFileDataKeyProp(KiprisBackFileDataKeyProp):
    def __init__(self):
        super().__init__()
        self.index = "indexNo"
        self.title = "title"
        self.legal_status_desc = "applicationStatus"
        self.drawing = "drawing"
