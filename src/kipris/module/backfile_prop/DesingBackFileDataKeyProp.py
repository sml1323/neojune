from ..core.KiprisBackFileDataKeyProp import KiprisBackFileDataKeyProp

class DesingBackFileDataKeyProp(KiprisBackFileDataKeyProp):
    def __init__(self):
        super().__init__()
        self.index = "number"
        self.title = "articleName"
        self.legal_status_desc = "applicationStatus"
        self.drawing = "imagePath"
