from ....kipris.core.parsing.KiprisParam import KiprisParam


class KiprisTestPram(KiprisParam):
    def __init__(self, app_no, applicant_id):
        super().__init__(app_no, applicant_id)
        self.name = "ok!"

class KiprisDesignPram(KiprisParam):
    def __init__(self, app_no, applicant_id):
        super().__init__(app_no, applicant_id)
        self.applicantName = app_no
        self.startNumber = 1
        self.etc = 'true'
        self.part = 'true'
        self.simi = 'true'
        self.abandonment = 'true'
        self.cancle = 'true'
        self.destroy = 'true'
        self.invalid = 'true'
        self.notice = 'true'
        self.open = 'true'
        self.registration = 'true'
        self.rejection = 'true'
        self.descSort = 'true'


def main():
    if True:
        param = KiprisTestPram("123456", "123456")

        print(param.get_dict())
        # 출력 결과
        # {'accessKey': 'gT7GE2pCd0zkrFsa=s9/vbar0=서비스코드', 'docsCount': 500, 'name': 'ok!'}

        print(param.get_dict_with_properties())
        # 출력 결과
        # {'accessKey': 'gT7GE2pCd0zkrFsa=s9/vbar0=서비스코드', 'app_no': '123456', 'applicant_id': '123456', 'docsCount': 500, 'name': 'ok!'}


    if True:
        design_param = KiprisDesignPram("123456", "123456")

        print(design_param.get_dict())
        # 출력 결과
        # {'accessKey': 'gT7qoU0dWQGE2pCd0zkrhnxsvaBXkljFsa=s9/vbar0=', 'docsCount': 500, 'applicantName': '123456', 'startNumber': 1, 'etc': 'true', 'part': 'true', 'simi': 'true', 'abandonment': 'true', 'cancle': 'true', 'destroy': 'true', 'invalid': 'true', 'notice': 'true', 'open': 'true', 'registration': 'true', 'rejection': 'true', 'descSort': 'true'}

        print(design_param.get_dict_with_properties())
        # 출력 결과
        # {'abandonment': 'true', 'accessKey': 'gT7qoU0dWQGE2pCd0zkrhnxsvaBXkljFsa=s9/vbar0=', 'app_no': '123456', 'applicantName': '123456', 'applicant_id': '123456', 'cancle': 'true', 'descSort': 'true', 'destroy': 'true', 'docsCount': 500, 'etc': 'true', 'invalid': 'true', 'notice': 'true', 'open': 'true', 'part': 'true', 'registration': 'true', 'rejection': 'true', 'simi': 'true', 'startNumber': 1}