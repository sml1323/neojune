from ....kipris.convert.mapper.DesignKiprisMapper import DesignKiprisMapper
from ....kipris.convert.mapper.PatentKiprisMapper import PatentKiprisMapper
from ....kipris.convert.mapper.TrademarkKiprisMapper import TrademarkKiprisMapper

from ....kipris.convert.converter.KiprisDesignXmlToDictConverter import KiprisDesignXmlToDictConverter
from ....kipris.convert.converter.KiprisPatentXmlToDictConverter import KiprisPatentXmlToDictConverter
from ....kipris.convert.converter.KiprisTrademarkXmlToDictConverter import KiprisTrademarkXmlToDictConverter

from ....util import util


def main():
    # 매핑 사전 정의
    design_mapping = DesignKiprisMapper().get_dict()
    patent_mapping = PatentKiprisMapper().get_dict()
    trademark_mapping = TrademarkKiprisMapper().get_dict()
    util.add_sys_path()
    # XML 파일 이름 설정
    # base_path = f"res/output/{util.get_timestamp()}"
    base_path = f"src/test/kipris/convert/xml"
    design_xml_filename = f'{base_path}/design.xml'  # XML 파일 경로
    patent_xml_filename = f'{base_path}/patent.xml'  # XML 파일 경로
    trademark_xml_filename = f'{base_path}/trademark.xml'  # XML 파일 경로

    if False:
        print("#### design_parser")
        design_parser = KiprisDesignXmlToDictConverter(design_mapping, design_xml_filename)
        design_results = design_parser.parse()
        print(design_results)
        print("")
        print("")

    if True:
        print("#### patent_parser")
        patent_parser = KiprisPatentXmlToDictConverter(patent_mapping, patent_xml_filename)
        patent_results = patent_parser.parse()
        print(patent_results)
        print("")
        print("")

    if False:
        print("#### trademark_parser")
        trademark_parser = KiprisTrademarkXmlToDictConverter(trademark_mapping, trademark_xml_filename)
        trademark_results = trademark_parser.parse()
        print(trademark_results)
        print("")
        print("")

# 출력 결과
'''
[
    {
        'applicant_id': '', 'ipr_code': '10', 'title': '생검용 포셉', 'serial_no': '1', 'applicant': '주식회사 파인메딕스', 'appl_no': '1020220161874', 'appl_date': '20221128', 'pub_num': 'None', 'pub_date': 'None', 'legal_status_desc': '공개', 'image_path': 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e22d01c5c32ba711cf10a74ba89bb6f6121e4a13175035888584660e7d1f78c29494ec46eec1ed75926f8d35e4b593bced3c93cbeaabf20739ce3cec11cb9dea92', 'reg_no': 'None', 'reg_date': 'None', 'open_no': '1020240079017', 'open_date': '20240604', 'main_ipc': 'A61B 10/06', 'abstract': '본 발명은 생검용 포셉에 관한 것으로, 보다 상세하게는 집게부, 연장코일, 핸들, 슬라이드 및 와이어를 포함하되, 집게부는 각각 복수의 치형이 형성되어 서로 맞물리는 한 쌍의 컵을 포함하고, 각각의 컵이 집게부가 닫친 상태에서 제1 컵 및 제2 컵 각각의 끝단은 서로 맞물리되, 각각의 컵에 형성된 치형 사이 거리가 컵의 끝단으로부터 연장코일 방향으로 점차 넓어지도록 형성되어, 채취하고자 하는 생체 조직을 효율적으로 절단하여 채취하는 생검용 포셉에 관한 것이다.'
    }, 
    {
        'applicant_id': '', 'ipr_code': '20', 'title': '내시경용 클리핑 장치', 'serial_no': '2', 'applicant': '주식회사 파인메딕스', 'appl_no': '2020230000297', 'appl_date': '20230214', 'pub_num': 'None', 'pub_date': 'None', 'legal_status_desc': '공개', 'image_path': 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e22d01c5c32ba711cf1a452232145a60d0b8266da58814264234883381b11bd2a4da8b9dc81ac1acc0d77b2695912fd1f5441ddeb0abe1034b68835d5e7437a2a8', 'reg_no': 'None', 'reg_date': 'None', 'open_no': '2020240001417', 'open_date': '20240821', 'main_ipc': 'A61B 17/128', 'abstract': '본 고안은 조작부가 간단하며, 클립의 결찰 및 분리 동작이 정확하여 내시경을 통해 이루어지는 생체 조직 지혈 및 봉합에 용이한 내시경용 클리핑 장치에 관한 것으로, 본 고안의 일 실시예에 따른 내시경용 클리핑 장치는, 지혈 또는 봉합이 요구되는 생체 조직의 병변 부위에 결찰 또는 분리되기 위해 한 쌍의 클립 암부 및 파지부와, 상기 한 쌍의 클립 암부와 연결되면서 가이드홈을 형성하는 윈위단 세그먼트가 구비된 클립; 코일링이 내부에 배치되는 핸들과, 상기 핸들상에서 전진 또는 후진이 가능한 슬라이더가 구비되며, 상기 슬라이더의 조작을 통해 상기 한 쌍의 클립 암부가 개폐되도록 하는 조작부; 상기 조작부의 구동을 상기 클립으로 전달하기 위한 모노 와이어 및 로프 와이어와, 상기 로프 와이어와 후크를 결속시키기 위한 로프 커플링과, 상기 코일링과 결속되는 것을 통해 상기 핸들에 조립되는 라운드 코일이 구비된 전달부; 상기 후크가 내부에 배치되며, 상기 원위단 세그먼트의 일부가 삽입되도록 일단 개방형으로 가공된 하우징과, 상기 원위단 세그먼트의 가이드홈 및 상기 하우징을 동시에 관통하여 상기 클립을 고정하면서 상기 클립의 개폐를 가이드하기 위한 하우징핀이 구비된 클립 결합부; 및 상기 라운드 코일을 감싸 일부가 상기 핸들의 내부에 배치되되, 나머지 부분이 시술 시 체내에 진입되는 제1 이너 시스가 구비된 ...(이하생략)'
    }, 
    {
        'applicant_id': '', 'ipr_code': '10', 'title': '내시경용 하이브리드 나이프', 'serial_no': '3', 'applicant': '주식회사 파인메딕스|울산대학교 산학협력단|재단법인 아산사회복지재단', 'appl_no': '1020170074427', 'appl_date': '20170613', 'pub_num': 'None', 'pub_date': '20190930', 'legal_status_desc': '등록', 'image_path': 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e22d01c5c32ba711cf8f228fe2f189efd810c362a82a2f8776640f7be4a2b838793d995848b3eff19a4616679d898d247608cd31536eb12d677fd0f85bbb063804', 'reg_no': '1020269380000', 'reg_date': '20190924', 'open_no': '1020180135754', 'open_date': '20181221', 'main_ipc': 'A61B 18/14', 'abstract': '본 발명은 서로 다른 종류의 나이프를 포함하여 교체 없이도 수직 및 수평 방향으로 점막하의 조직을 용이하게 절개 및 박리 가능한 내시경용 하이브리드 나이프에 관한 것으로, 본 발명은, 중공을 갖으며, 일측에는 상기 중공에 연결된 개구부가 형성된 핸들부와, 상기 핸들부의 외주면에 길이 방향을 따라 전, 후방 슬라이드가 가능하도록 결합된 제1 및 제2 핸들 슬라이더와, 상기 핸들부의 중공에 배치되며 상기 제1 핸들 슬라이더와 일체로 이동 가능하도록 연결된 파이프와, 상기 파이프를 관통하도록 배치되며 상기 제2 핸들 슬라이더와 일체로 이동 가능하도록 연결된 제2 나이프와, 상기 핸들부의 일단에 결합되며, 내부로 유체를 주입하기 위한 유체 주입부와, 상기 유체 주입부의 일단에 연결되며 내부에는 상기 파이프가 배치되는 이너 튜브와, 상기 파이프의 끝단에 결합되는 제1 나이프 및 상기 제1 나이프의 끝단에 결합되는 절연성 팁(tip)을 포함하며, 상기 제1 나이프와 제2 나이프는 서로 독립적으로 슬라이드 이동 가능한 것을 특징으로 하는 내시경용 하이브리드 나이프를 제공한다.'
    }
]
'''
        


if __name__ == "__main__":
    main()  # 메인 함수 실행
