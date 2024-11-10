class KiprisObject:
    def get_dict(self) -> dict:
        """객체를 딕셔너리 형태로 변환합니다.
        Returns:
            dict: 객체의 속성들을 담고 있는 딕셔너리
        """
        attributes = {}
        for key, value in vars(self).items():
            # 키가 '_'로 시작하지 않는 것만 추가
            if not key.startswith('_'):
                attributes[key] = value
        return attributes

    def get_dict_with_properties(self) -> dict:
        # 모든 속성명을 가져옴
        attributes = dir(self)
        result = {}

        # 속성명 하나씩 반복해서 확인
        for name in attributes:
            # 속성이 비공개 속성(밑줄로 시작)인지, 함수가 아닌지 체크
            if not name.startswith('_') and not callable(getattr(self, name)):
                # 속성을 접근하여 딕셔너리에 추가
                result[name] = getattr(self, name)

        return result
