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


def run():
    # param.main()
    # fetcher_data.main()
    # fetcher.main()
    # applicant_info_fetcher.main()
    # xml_to_dict_converter.main()
    # uploader.main()
    # all_conn.main()
    # blocked_users.main()
    util.send_slack_message("neojune", save_to_xml.main)
    util.send_slack_message("neojune", save_to_xml.main, "TB24_210", "university")
    # asyncio.run(save_to_xml.main())
    # asyncio.run(save_to_xml.main("TB24_210", "university"))
    # save_to_xml.main()
    pass
