from ....kipris.core.convert.KiprisXmlDumpDataQueryBuilder import KiprisXmlDumpDataQueryBuilder
from ....kipris.convert.mapper.KiprisDesignMapper import KiprisDesignMapper
from ....kipris.convert.mapper.KiprisPatentMapper import KiprisPatentMapper
from ....kipris.convert.mapper.KiprisTrademarkMapper import KiprisTrademarkMapper

from ....kipris.convert.converter.KiprisDesignXmlToDictConverter import KiprisDesignXmlToDictConverter
from ....kipris.convert.converter.KiprisPatentXmlToDictConverter import KiprisPatentXmlToDictConverter
from ....kipris.convert.converter.KiprisTrademarkXmlToDictConverter import KiprisTrademarkXmlToDictConverter

from ....util import util



def main():
    base_path = f"src/test/kipris/convert/xml"
    design_xml_filename = f'{base_path}/design.xml'  # XML 파일 경로

    # design_converter = KiprisDesignXmlToDictConverter(KiprisDesignMapper(), design_xml_filename)
    # print(design_converter.parse())
    printer = KiprisXmlDumpDataQueryBuilder(
        table_name="TB24_company_design", 
        xml_filename=design_xml_filename,
        xml_to_dict_converter_class=KiprisDesignXmlToDictConverter, 
    )
    # printer.append()
    printer.print_sql_file()
    # print(sql)
    pass