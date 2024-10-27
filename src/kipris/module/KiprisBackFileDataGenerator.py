from .core.KiprisObject import KiprisObject
from .core.KiprisBackFileDataKeyProp import KiprisBackFileDataKeyProp
from .core.KiprisParams import KiprisParams


class KiprisBackFileDataGenerator(KiprisObject):
    def __init__(self, params: KiprisParams, key_prop:KiprisBackFileDataKeyProp):
        super().__init__()
        self.params = params
        self.key_prop = key_prop.get_dict()

    def create(self, item: list) -> list:
        res = []
        for i in item:
            res.append({})
            for key, value in self.key_prop.items():
                res[-1][key] = None
                if(value != None and value in i): 
                    res[-1][key] = i[value]
                elif(key == "applicant"):
                    res[-1][key] = self.params.applicantName
        return res