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
            # dir()을 써서 인스턴스의 모든 속성을 다 가져오고, property 속성도 추가함
            return {name: getattr(self, name) for name in dir(self) 
                    if not name.startswith('_') and not callable(getattr(self, name))}