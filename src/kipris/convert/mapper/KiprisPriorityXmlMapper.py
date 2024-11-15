from ...core.convert.KiprisSubXmlMapper import KiprisSubXmlMapper

class KiprisPriorityXmlMapper(KiprisSubXmlMapper):
    def __init__(self):
        super().__init__()
        self.ipr_type = "ipr_type" # design, trademark
        self.priority_date = 'priority_date'
        self.priority_no = 'priority_no'