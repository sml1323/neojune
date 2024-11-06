import os
from ...kipris.convert.mapper.DesignKiprisMapper import DesignKiprisMapper
from ...kipris.convert.mapper.PatentKiprisMapper import PatentKiprisMapper
from ...kipris.convert.mapper.TrademarkKiprisMapper import TrademarkKiprisMapper

from ...kipris.convert.converter.KiprisDesignXmlToDictConverter import KiprisDesignXmlToDictConverter
from ...kipris.convert.converter.KiprisPatentXmlToDictConverter import KiprisPatentXmlToDictConverter
from ...kipris.convert.converter.KiprisTrademarkXmlToDictConverter import KiprisTrademarkXmlToDictConverter

from ...kipris.upload.uploader.KiprisTB24DesignDataUploader import KiprisTB24DesignDataUploader
from ...kipris.upload.uploader.KiprisTB24PatentDataUploader import KiprisTB24PatentDataUploader
from ...kipris.upload.uploader.KiprisTB24TrademarkDataUploader import KiprisTB24TrademarkDataUploader


from ...util import util



def main():
   
    # 매핑 사전 정의
    design_mapping = DesignKiprisMapper().get_dict()
    patent_mapping = PatentKiprisMapper().get_dict()
    trademark_mapping = TrademarkKiprisMapper().get_dict()
    util.add_sys_path()
    # XML 파일 이름 설정
    base_path = f"{os.path.dirname(os.path.abspath(__file__))}/xml"
    design_xml_filename = f'{base_path}/design.xml'  # XML 파일 경로
    patent_xml_filename = f'{base_path}/patent.xml'  # XML 파일 경로
    trademark_xml_filename = f'{base_path}/trademark.xml'  # XML 파일 경로

    if False:
        print("#### design")
        design_parser = KiprisDesignXmlToDictConverter(design_mapping, design_xml_filename)
        design_results = design_parser.parse()
        KiprisTB24DesignDataUploader().upload(design_results)


    if False:
        print("#### patent")
        patent_parser = KiprisPatentXmlToDictConverter(patent_mapping, patent_xml_filename)
        print(patent_parser.parse())
        # patent_results = patent_parser.parse()
        # KiprisTB24PatentDataUploader().upload(patent_results)


    if True:
        print("#### trademark")
        trademark_parser = KiprisTrademarkXmlToDictConverter(trademark_mapping, trademark_xml_filename)
        # trademark_results = trademark_parser.parse()
        # KiprisTB24TrademarkDataUploader().upload(trademark_results)
        


if __name__ == "__main__":
    main()  # 메인 함수 실행
