from .kipris.parsing import param
from .kipris.parsing import fetcher_data
from .kipris.parsing import fetcher
from .kipris.parsing import applicant_info_fetcher
from .kipris.convert import xml_to_dict_converter
from .kipris.upload import uploader

def run():
    # param.main()
    # fetcher_data.main()
    # fetcher.main()
    # applicant_info_fetcher.main()
    # xml_to_dict_converter.main()
    uploader.main()
