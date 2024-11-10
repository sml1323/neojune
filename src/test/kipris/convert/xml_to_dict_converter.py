import time 

from ....kipris.convert.mapper.DesignKiprisMapper import DesignKiprisMapper
from ....kipris.convert.mapper.PatentKiprisMapper import PatentKiprisMapper
from ....kipris.convert.mapper.TrademarkKiprisMapper import TrademarkKiprisMapper

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
        design_mapping = DesignKiprisMapper()
        design_xml_filename = f'{base_path}/design.xml'  # XML 파일 경로
        design_parser = KiprisDesignXmlToDictConverter(design_mapping, design_xml_filename)
        design_results = design_parser.parse()
        print(len(design_results))
        print(design_results)

    def patent_action():
        patent_mapping = PatentKiprisMapper()
        patent_xml_filename = f'{base_path}/patent.xml'  # XML 파일 경로
        patent_parser = KiprisPatentXmlToDictConverter(patent_mapping, patent_xml_filename)
        patent_results = patent_parser.parse()
        print(len(patent_results))
        print(patent_results)

    def trademark_action():
        trademark_mapping = TrademarkKiprisMapper()
        trademark_xml_filename = f'{base_path}/trademark.xml'  # XML 파일 경로
        trademark_parser = KiprisTrademarkXmlToDictConverter(trademark_mapping, trademark_xml_filename)
        trademark_results = trademark_parser.parse()
        print(len(trademark_results))
        print(trademark_results)


    # util.execute_with_time("#### design_parser", design_action)
    util.execute_with_time("#### patent_parser", patent_action)
    # util.execute_with_time("#### trademark_parser", trademark_action)


if __name__ == "__main__":
    main()  # 메인 함수 실행
