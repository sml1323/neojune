from ..KiprisObject import KiprisObject

class KiprisSubProp(KiprisObject):
    def __init__(self):
        super().__init__()
        self.ipr_seq = None
        # self._applicant_id = None
        # self._serial_no = None
        # self._appl_no = None

    # @property
    # def applicant_id(self):
    #     return self._applicant_id

    # @applicant_id.setter
    # def applicant_id(self, value):
    #     self._applicant_id = value

    # @property
    # def serial_no(self):
    #     return self._serial_no

    # @serial_no.setter
    # def serial_no(self, value):
    #     self._serial_no = value

    # @property
    # def appl_no(self):
    #     return self._appl_no

    # @appl_no.setter
    # def appl_no(self, value):
    #     self._appl_no = value

    @property
    def ipr_seq(self):
        return self._ipr_seq

    @ipr_seq.setter
    def ipr_seq(self, value):
        self._ipr_seq = value

    def __getitem__(self, key):
        # 해당 key에 맞는 속성 값 반환
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        # 해당 key에 value를 설정
        setattr(self, key, value)
    
    def __iter__(self):
        # (속성 이름, 속성 값) 형태의 튜플들을 순회하게 함
        for attr, value in self.get_dict_with_properties().items():
            yield attr, value