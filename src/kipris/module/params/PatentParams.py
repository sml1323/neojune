from ..core.KiprisParams import KiprisParams
from ..core.ServiceNames import ServiceNames


class PatentParams(KiprisParams):
    def __init__(self):
        super().__init__(serviceName=ServiceNames.PATENT)

