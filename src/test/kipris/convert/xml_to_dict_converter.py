import time 

from ....kipris.convert.mapper.KiprisDesignMapper import KiprisDesignMapper
from ....kipris.convert.mapper.KiprisPatentMapper import KiprisPatentMapper
from ....kipris.convert.mapper.KiprisTrademarkMapper import KiprisTrademarkMapper

from ....kipris.convert.converter.KiprisDesignXmlToDictConverter import KiprisDesignXmlToDictConverter
from ....kipris.convert.converter.KiprisPatentXmlToDictConverter import KiprisPatentXmlToDictConverter
from ....kipris.convert.converter.KiprisTrademarkXmlToDictConverter import KiprisTrademarkXmlToDictConverter

from ....util import util


def main():
    # 매핑 사전 정의
    
    
    
    util.add_sys_path()
    # XML 파일 이름 설정
    # base_path = f"res/output/{util.get_timestamp()}"
    base_path = f"src/test/kipris/convert/xml"
    
    
    

    def design_action():
        design_xml_filename = f'{base_path}/design.xml'  # XML 파일 경로
        design_parser = KiprisDesignXmlToDictConverter(design_xml_filename)
        design_results = design_parser.parse()
        print(len(design_results))
        print(design_results)

    def patent_action():
        patent_xml_filename = f'{base_path}/patent.xml'  # XML 파일 경로
        patent_parser = KiprisPatentXmlToDictConverter(patent_xml_filename)
        patent_results = patent_parser.parse()
        print(len(patent_results))
        print(patent_results)

    def trademark_action():
        trademark_xml_filename = f'{base_path}/trademark.xml'  # XML 파일 경로
        trademark_parser = KiprisTrademarkXmlToDictConverter(trademark_xml_filename)
        trademark_results = trademark_parser.parse()
        print(len(trademark_results))
        print(trademark_results)


    util.execute_with_time("#### design_parser", design_action)
    util.execute_with_time("#### patent_parser", patent_action)
    util.execute_with_time("#### trademark_parser", trademark_action)

## 출력
'''
## design_action
{
    'agent': '최경수',
    'appl_date': '20140408',
    'appl_no': '3020140017534',
    'applicant': '주식회사 파인메딕스|전성우',
    'applicant_id': '2',
    'image_path': 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e29e0b68f68d514bb0fedbb1325566a2d358de5f2bd287de10331b3d1887947c482a970947ddae1bf2bf9cda621bd8ba0d7223906319bd9903',
    'inventor': '전성우',
    'ipr_code': '30',
    'ipr_seq': '',
    'legal_status_desc': '등록',
    'open_date': 'None',
    'open_no': 'None',
    'pub_date': '20141205',
    'pub_num': 'None',
    'reg_date': '20141201',
    'reg_no': '3007743290000',
    'serial_no': '1',
    'title': '내시경시술용 핸들'
},


## patent_action
{
    'abstract': '본 발명은 생검용 포셉에 관한 것으로, 보다 상세하게는 집게부, 연장코일, 핸들, 슬라이드 및 와이어를 포함하되, 집게부는 각각 복수의 치형이 형성되어 서로 맞물리는 한 쌍의 컵을 포함하고, 각각의 컵이 집게부가 닫친 상태에서 제1 컵 및 제2 컵 각각의 끝단은 서로 맞물리되, 각각의 컵에 형성된 치형 사이 거리가 컵의 끝단으로부터 연장코일 방향으로 점차 넓어지도록 형성되어, 채취하고자 하는 생체 조직을 효율적으로 절단하여 채취하는 생검용 포셉에 관한 것이다.',
    'appl_date': '20221128',
    'appl_no': '1020220161874',
    'applicant': '주식회사 파인메딕스',
    'applicant_id': '2',
    'image_path': 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e22d01c5c32ba711cf10a74ba89bb6f6121e4a13175035888584660e7d1f78c29494ec46eec1ed75926f8d35e4b593bced3c93cbeaabf20739ce3cec11cb9dea92',
    'ipr_code': '10',
    'ipr_seq': '',
    'legal_status_desc': '공개',
    'main_ipc': 'A61B 10/06',
    'open_date': '20240604',
    'open_no': '1020240079017',
    'pub_date': 'None',
    'pub_num': 'None',
    'reg_date': 'None',
    'reg_no': 'None',
    'serial_no': '1',
    'title': '생검용 포셉'
}

## trademark_action
{
    'agent': '최경수',
    'appl_date': '20130308',
    'appl_no': '4120130008475',
    'applicant': '주식회사 파인메딕스',
    'applicant_id': '2',
    'image_path': 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ad7a17eeeef6e4ea4b5e22ef00dd3e290e6d58d1e0f7f5bf704c6426ac458a3ceee61a4b05d294db020be58df77f8ea8',
    'ipr_code': '41',
    'ipr_seq': '',
    'legal_status_desc': '등록',
    'pub_date': '20140204',
    'pub_num': '4120140009693',
    'serial_no': '1',
    'title': '|주|파인메딕스 FINEMEDIX'
},
'''


if __name__ == "__main__":
    main()  # 메인 함수 실행
