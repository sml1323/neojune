from .core.KiprisObject import KiprisObject
from .core.KiprisBackFileDataKeyProp import KiprisBackFileDataKeyProp
from .core.KiprisParams import KiprisParams


class KiprisBackFileDataGenerator(KiprisObject):
    """
    KIPRIS 백파일 데이터 생성기.

    Attributes:
        params (KiprisParams): KIPRIS 파라미터.
        key_prop (dict): 백파일 데이터 키 속성 딕셔너리.
    """
    def __init__(self, params: KiprisParams, key_prop:KiprisBackFileDataKeyProp):
        """
        KIPRIS 백파일 데이터 생성기를 초기화합니다.

        Args:
            params (KiprisParams): KIPRIS 파라미터.
            key_prop (KiprisBackFileDataKeyProp): 백파일 데이터 키 속성.
        """
        super().__init__()
        self.params = params
        self.key_prop = key_prop.get_dict()

    def create(self, item: list) -> list:
        """
        주어진 아이템 목록을 기반으로 백파일 데이터를 생성합니다.
        Args:
            item (list): 백파일 데이터를 생성할 아이템 목록.

        Returns:
            list: 생성된 백파일 데이터 목록.
        """
        res = []
        for i in item:
            res.append({})
            for key, value in self.key_prop.items():
                # 기본값 설정
                res[-1][key] = None
                # key_prop에 정의된 value가 item에 존재하는 경우 해당 값으로 설정
                if(value != None and value in i): 
                    res[-1][key] = i[value]
                # applicant의 경우 params에서 가져오도록 설정
                elif(key == "applicant"):
                    res[-1][key] = self.params.applicantName
        return res