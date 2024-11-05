from ...kipris.convert.mapper.DesignKiprisMapper import DesignKiprisMapper
from ...kipris.convert.mapper.PatentKiprisMapper import PatentKiprisMapper
from ...kipris.convert.mapper.TrademarkKiprisMapper import TrademarkKiprisMapper

from ...kipris.convert.converter.KiprisDesignXmlToDictConverter import KiprisDesignXmlToDictConverter
from ...kipris.convert.converter.KiprisPatentXmlToDictConverter import KiprisPatentXmlToDictConverter
from ...kipris.convert.converter.KiprisTrademarkXmlToDictConverter import KiprisTrademarkXmlToDictConverter

from ...util import util

def main():
    # 매핑 사전 정의
    design_mapping = DesignKiprisMapper().get_dict()
    patent_mapping = PatentKiprisMapper().get_dict()
    trademark_mapping = TrademarkKiprisMapper().get_dict()
    util.add_sys_path()
    # XML 파일 이름 설정
    # base_path = f"res/output/{util.get_timestamp()}"
    base_path = f"src/test/xml_to_dict/xml"
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

        


if __name__ == "__main__":
    main()  # 메인 함수 실행
