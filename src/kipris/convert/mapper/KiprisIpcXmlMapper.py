from ...core.convert.KiprisSubXmlMapper import KiprisSubXmlMapper

class KiprisIpcXmlMapper(KiprisSubXmlMapper):
    def __init__(self):
        super().__init__()
        self.ipc_cpc = "ipc_cpc"
        self.ipc_cpc_code = "ipc_cpc_code"