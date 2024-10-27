from ..core.KiprisBackFileDataKeyProp import KiprisBackFileDataKeyProp

class PatentBackFileDataKeyProp(KiprisBackFileDataKeyProp):
    def __init__(self):
        super().__init__()
        self.index = "indexNo"
        self.title = "inventionTitle"
        self.legal_status_desc = "registerStatus"
        self.drawing = "drawing"
