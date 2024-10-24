class KiprisObject:
    def get_dict(self) -> dict:
        """객체를 딕셔너리 형태로 변환합니다.
        Returns:
            dict: 객체의 속성들을 담고 있는 딕셔너리
        """
        return vars(self)
