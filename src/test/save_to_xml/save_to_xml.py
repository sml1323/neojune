import asyncio
from ...db.mysql import Mysql
from ...kipris.parsing.xml.KiprisXmlDataGenerator import KiprisXmlDataGenerator
from ...kipris.parsing.fetcher.KiprisPatentFetcher import KiprisPatentFetcher
from ...kipris.parsing.fetcher.KiprisDesignFetcher import KiprisDesignFetcher
from ...kipris.parsing.fetcher.KiprisTrademarkFetcher import KiprisTrademarkFetcher
from ...util import util
from ...util import monitoring
mysql = Mysql()

class Info():
    def __init__(self):
        self.patent = None
        self.design = None
        self.trademark = None


async def main(table_name="TB24_200", dir_path="xml/company"):
    print(table_name)
    async def get_info() -> Info:
        info = Info()
        if table_name == "TB24_200":
            company_logger = monitoring.setup_logger("company")
            company_logger.debug("TB24_200")
            # applicant_numbers = mysql.get_all_company_no_id()
            # applicant_numbers = mysql.get_limit_company_no_id(5)
            # p3: 120080091393,  p23: 120070509242
            # applicant_numbers = [[120070509242, 10],[120080091393, 20]]
            applicant_numbers = [[120140558200, 1]]
        else:
            university_logger = monitoring.setup_logger("university")
            university_logger.debug("TB24_210")
            # applicant_numbers = mysql.get_all_university_no_seq()
            # applicant_numbers = mysql.get_limit_university_no_seq(5)
            applicant_numbers = [[220050095099, 1]]

        async def patent_action_api():
            patent_fetcher = KiprisPatentFetcher(applicant_numbers)
            return await patent_fetcher.get_infos("patent")
    
        async def design_action_api():
            design_fetcher = KiprisDesignFetcher(applicant_numbers)
            return await design_fetcher.get_infos("design")
    
        async def trademark_action_api():
            trademark_fetcher = KiprisTrademarkFetcher(applicant_numbers)
            return await trademark_fetcher.get_infos("trademark")
        
        info.patent = await util.execute_with_time_async("patent_action_api", patent_action_api)
        info.design = await util.execute_with_time_async("design_action_api", design_action_api)
        info.trademark = await util.execute_with_time_async("trademark_action_api", trademark_action_api)
        return info

    info:Info = await util.execute_with_time_async("`전체 호출 완료: 3개 신청자 처리", get_info)
    
    print("===========================================")

    async def save_xml(info:Info):
        kipris_xml_dataGenerator = KiprisXmlDataGenerator()
        async def action_patent():
            kipris_xml_dataGenerator.append_data_lists(info.patent)
            kipris_xml_dataGenerator.apply()
            kipris_xml_dataGenerator.save(f"patent", dir_path)
        
        async def action_design():
            kipris_xml_dataGenerator.append_data_lists(info.design)
            kipris_xml_dataGenerator.apply()
            kipris_xml_dataGenerator.save(f"design", dir_path)
        
        async def action_trademark():
            kipris_xml_dataGenerator.append_data_lists(info.trademark)
            kipris_xml_dataGenerator.apply()
            kipris_xml_dataGenerator.save(f"trademark", dir_path)

        await util.execute_with_time_async("### patent xml save", action_patent)
        await util.execute_with_time_async("### design xml save", action_design)
        await util.execute_with_time_async("### trademark xml save", action_trademark)


    await util.execute_with_time_async("xml 저장 완료", save_xml, info)


from ...kipris.parsing.fetcher.KiprisPatentChangeFetcher import KiprisPatentChangeFetcher
from ...kipris.parsing.fetcher.KiprisPatentApplicationFetcher import KiprisPatentApplicationFetcher
from ...kipris.parsing.fetcher.KiprisPatentApplicantFetcher import KiprisPatentApplicantFetcher
from ...kipris.parsing.fetcher.KiprisDesignApplicationFetcher import KiprisDesignApplicationFetcher
from ...kipris.parsing.fetcher.KiprisDesignApplicantFetcher import KiprisDesignApplicantFetcher
from ...kipris.parsing.fetcher.KiprisTrademarkApplicationFetcher import KiprisTrademarkApplicationFetcher
from ...kipris.parsing.fetcher.KiprisTrademarkApplicantFetcher import KiprisTrademarkApplicantFetcher
async def daliy():

    company_dict = mysql.get_all_company_no_id(is_dict=True)
    university_dict = mysql.get_all_university_no_seq(is_dict=True)

    async def patent_change_api():
        # patent_fetcher = KiprisPatentChangeFetcher()
        # change_patent = await patent_fetcher.get_info()
        change_patent = ['2020040031672', '1020150008784', '1020170175877','1020190062722', '1020237020473','1020217004391' ]
        patent_fetcher = KiprisPatentApplicantFetcher(change_patent)

        await patent_fetcher.get_infos("patent_daliy")
        comp_patent_list = patent_fetcher.applicant_list_db(company_dict)
        univ_patent_list = patent_fetcher.applicant_list_db(university_dict)

        print("com" , comp_patent_list)
        print("uni", univ_patent_list)
        comp_patent_list = [['2020040031672', 4719], ['1020150008784', 4719]]
        univ_patent_list = [['1020170175877', 1]]

        applicant_fetcher_comp = KiprisPatentApplicationFetcher(comp_patent_list)
        comp_result = await applicant_fetcher_comp.get_infos("patent")
        applicant_fetcher_univ = KiprisPatentApplicationFetcher(univ_patent_list)
        univ_result = await applicant_fetcher_univ.get_infos("design")

        kipris_xml_comp_dataGenerator = KiprisXmlDataGenerator()
        kipris_xml_comp_dataGenerator.append_data_lists(comp_result)
        kipris_xml_comp_dataGenerator.apply()
        kipris_xml_comp_dataGenerator.save(f"patent", "xml/company")
        kipris_xml_univ_dataGenerator = KiprisXmlDataGenerator()
        kipris_xml_univ_dataGenerator.append_data_lists(univ_result)
        kipris_xml_univ_dataGenerator.apply()
        kipris_xml_univ_dataGenerator.save(f"patent", "xml/university")
    
    async def design_change_api():
        # design_fetcher = KiprisDesignChangeFetcher()
        # change_design = await design_fetcher.get_info()
        change_design = ['3020240008715', '3020240027877','3020240000641','3020000008117','3020230034586','3020240029394','3020230045204','3020100016654','3020240008442','3020240040451','3020240004483','3020140033290','3020240018854','3020240013706','3020150032691','3020080033557','3020237001747','3020240029397','3019940003203','3020140025785','3020240004786','3020247000500','3020190035008','3020010032919','3020160056068','3019990002670',]
        design_fetcher = KiprisDesignApplicantFetcher(change_design)

        await design_fetcher.get_infos("design_daliy")

        comp_design_list = design_fetcher.applicant_list_db(company_dict)
        univ_design_list = design_fetcher.applicant_list_db(university_dict)

        print("com" , comp_design_list)
        print("uni", univ_design_list)
        comp_design_list = [['3020000008117', 826], ['3020240029394', 3554], ['3020100016654', 826], ['3020240029397', 3554]]
        univ_design_list = [['3020240004483', 319], ['3020160056068', 319]]

        applicant_fetcher_comp = KiprisDesignApplicationFetcher(comp_design_list)
        comp_result = await applicant_fetcher_comp.get_infos("design")
        applicant_fetcher_univ = KiprisDesignApplicationFetcher(univ_design_list)
        univ_result = await applicant_fetcher_univ.get_infos("design")

        kipris_xml_com_dataGenerator = KiprisXmlDataGenerator()
        kipris_xml_com_dataGenerator.append_data_lists(comp_result)
        kipris_xml_com_dataGenerator.apply()
        kipris_xml_com_dataGenerator.save(f"design", "xml/company")
        kipris_xml_univ_dataGenerator = KiprisXmlDataGenerator()
        kipris_xml_univ_dataGenerator.append_data_lists(univ_result)
        kipris_xml_univ_dataGenerator.apply()
        kipris_xml_univ_dataGenerator.save(f"design", "xml/university")

        
    async def trademark_change_api():
        # trademark_fetcher = KiprisTrademarkChangeFetcher()
        # change_trademark = await trademark_fetcher.get_info()
        change_trademark = ['4020207005051','4020240182047','4020240201617','4020230135281','4020230000432','4020230130474','4020200158108','4020240190406','4020207001387','4020230106511','4020100008431','4020230119103','4020230094158','4020240100053','4020240009833','4020197020798','4020230088243','4020207002511','4020207000102','4020230082882','4020080055728','4020230121744','4020200063953','4020230165986','4020230081094','4020230078790','4020207002552','4020210185421','4020230071382','4020230140541','4020230100346','4020230131019','4020230171683','4020240033432','4020240202594','4020230023070','4020230115991','4020197020367','4020207006045','4020237019233','4020177015105','4020230144944','4020230012494','4020057005429','4020240174026','4020207004584','4020200216269','4020230111876','4020240011111','4020230035024','4020230050843','4020230148450','4020197021632','4020240018794','4020237012055','4020240038640','4020230065042','4020230163101','4020207002342','4020240190662','4020230223325','4020230180648','4020207000364','4020207006140','4020197021198','4020237007209','4020230156352']
        trademark_fetcher = KiprisTrademarkApplicantFetcher(change_trademark)

        await trademark_fetcher.get_infos("trademark_daliy")
        comp_trademark_list = trademark_fetcher.applicant_list_db(company_dict)
        univ_trademark_list = trademark_fetcher.applicant_list_db(university_dict)

        print("com" , comp_trademark_list)
        print("uni", univ_trademark_list)
        comp_trademark_list = [['4020230035024', 5790], ['4020230156352', 5014]]
        univ_trademark_list = [['4020230223325', 236]]

        
        applicant_fetcher_com = KiprisTrademarkApplicationFetcher(comp_trademark_list)
        comp_result = await applicant_fetcher_com.get_infos("trademark")
        applicant_fetcher_com = KiprisTrademarkApplicationFetcher(univ_trademark_list)
        univ_result = await applicant_fetcher_com.get_infos("trademark")

        kipris_xml_comp_dataGenerator = KiprisXmlDataGenerator()
        kipris_xml_comp_dataGenerator.append_data_lists(comp_result)
        kipris_xml_comp_dataGenerator.apply()
        kipris_xml_comp_dataGenerator.save(f"trademark", "xml/company")
        kipris_xml_univ_dataGenerator = KiprisXmlDataGenerator()
        kipris_xml_univ_dataGenerator.append_data_lists(univ_result)
        kipris_xml_univ_dataGenerator.apply()
        kipris_xml_univ_dataGenerator.save(f"trademark", "xml/university")

    await util.execute_with_time_async("patent_change_api", patent_change_api)
    await util.execute_with_time_async("design_change_api", design_change_api)
    await util.execute_with_time_async("trademark_change_api", trademark_change_api)


if __name__ == '__main__':
    asyncio.run(main())
6