from ..core.KiprisParams import KiprisParams
from ..core.ServiceNames import ServiceNames

class DesingPrams(KiprisParams):
    def __init__(self):
        super().__init__(serviceName=ServiceNames.DESIGN)
        self.open = 'true'
        self.rejection = 'true'
        self.destroy = 'true'
        self.cancle = 'true'
        self.notice = 'true'
        self.registration = 'true'
        self.invalid = 'true'
        self.abandonment = 'true'
        self.simi = 'true'
        self.part = 'true'
        self.etc = 'true'
        self.sortSpec = 'applicationDate'
    
