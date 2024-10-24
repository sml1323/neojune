from .core.KiprisParams import KiprisParams

class DesingPrams(KiprisParams):
    def __init__(self, service_key):
        super().__init__(service_key)
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
    
