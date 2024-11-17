import asyncio,sys
from ..util import util
from .kipris.parsing import param
from .kipris.parsing import fetcher_data
from .kipris.parsing import fetcher
from .kipris.parsing import applicant_info_fetcher
from .kipris.convert import xml_to_dict_converter
from .kipris.upload import uploader
from .all_conn import all_conn
from .blocked_users import blocked_users
from src.util import util
from src.test.save_to_xml import save_to_xml
from src.test.kipris.convert import dict_to_sql
from src.test.kipris.convert import dict_to_sql_sub
from src.test.save_to_db import sql_to_db


def run():
    # param.main()
    # fetcher_data.main()
    # fetcher.main()
    # applicant_info_fetcher.main()
    # xml_to_dict_converter.main()
    # uploader.main()
    # all_conn.main()
    # blocked_users.main()
    # util.send_slack_message("neojune", save_to_xml.main) 
    # util.send_slack_message("neojune", save_to_xml.main, "TB24_210", "xml/university")
    # asyncio.run(save_to_xml.main())
    # asyncio.run(save_to_xml.main("TB24_210", "xml/university"))


    ### main table 저장 
    # util.execute_with_time("dict_to_sql", dict_to_sql.main)
    # util.execute_with_time("sql_to_db", sql_to_db.main)

    ### sub table 저장 
    util.execute_with_time("dict_to_sql", dict_to_sql_sub.main)
    # util.execute_with_time("sql_to_db", sql_to_db.main, False)
    pass
