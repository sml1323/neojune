import os, re
from lxml import etree
from typing import List, Dict
from ...kipris.convert.mapping.DesignKiprisMapping import DesignKiprisMapping
from ...kipris.convert.mapping.PatentKiprisMapping import PatentKiprisMapping
from ...kipris.convert.mapping.TrademarkKiprisMapping import TrademarkKiprisMapping

from ...kipris.convert.converter.KiprisDesignXmlToDictConverter import KiprisDesignXmlToDictConverter
from ...kipris.convert.converter.KiprisPatentXmlToDictConverter import KiprisPatentXmlToDictConverter
from ...kipris.convert.converter.KiprisTrademarkXmlToDictConverter import KiprisTrademarkXmlToDictConverter


def main():
    # 매핑 사전 정의

    design_mapping = DesignKiprisMapping().get_dict()

    patent_mapping = PatentKiprisMapping().get_dict()

    trademark_mapping = TrademarkKiprisMapping().get_dict()

    # XML 파일 이름 설정
    base_path = "/root/work/res/xml"
    design_xml_filename = f'{base_path}/design_data_20241028_195040.xml'  # XML 파일 경로
    patent_xml_filename = f'{base_path}/patent_data_20241028_195040.xml'  # XML 파일 경로
    trademark_xml_filename = f'{base_path}/trademark_data_20241028_195040.xml'  # XML 파일 경로

    if True:
        print("#### design_parser")
        design_parser = KiprisDesignXmlToDictConverter(design_mapping, design_xml_filename)
        design_results = design_parser.parse()
        print(design_results)
        print("")
        print("")

    if False:
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
