from ..KiprisObject import KiprisObject

class KiprisMapper(KiprisObject):
    def __init__(self):
        super().__init__()
        self._ipr_seq = None
        self._applicant_id = None
        # 분리
        self._ipr_code = None
        self._title = None
        self._serial_no = None
        self._applicant = None
        self._appl_no = None
        self._appl_date = None
        self._pub_num = None
        self._pub_date = None
        self._legal_status_desc = None
        self._image_path = None
    
    @property
    def ipr_seq(self):
        return self._ipr_seq

    @ipr_seq.setter
    def ipr_seq(self, value):
        self._ipr_seq = value

    @property
    def applicant_id(self):
        return self._applicant_id

    @applicant_id.setter
    def applicant_id(self, value):
        self._applicant_id = value

    @property
    def ipr_code(self):
        return self._ipr_code

    @ipr_code.setter
    def ipr_code(self, value):
        self._ipr_code = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value

    @property
    def applicant(self):
        return self._applicant

    @applicant.setter
    def applicant(self, value):
        self._applicant = value

    @property
    def appl_no(self):
        return self._appl_no

    @appl_no.setter
    def appl_no(self, value):
        self._appl_no = value

    @property
    def appl_date(self):
        return self._appl_date

    @appl_date.setter
    def appl_date(self, value):
        self._appl_date = value

    @property
    def pub_num(self):
        return self._pub_num

    @pub_num.setter
    def pub_num(self, value):
        self._pub_num = value

    @property
    def pub_date(self):
        return self._pub_date

    @pub_date.setter
    def pub_date(self, value):
        self._pub_date = value

    @property
    def legal_status_desc(self):
        return self._legal_status_desc

    @legal_status_desc.setter
    def legal_status_desc(self, value):
        self._legal_status_desc = value

    @property
    def image_path(self):
        return self._image_path

    @image_path.setter
    def image_path(self, value):
        self._image_path = value

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