import asyncio,sys
from src.test import test
from src.util import util
from src.test.save_to_xml import save_to_xml
# from src.test.xml_to_dict import xml_to_dict
# from src.test.dict_to_db import dict_to_db
# from util.util import send_slack_message
from src.util.util import send_slack_message

try:
    send_slack_message( "<!here> 사용 시작 : 윤재")
    asyncio.run(save_to_xml.main('TB24_200'))
finally:
    send_slack_message( "<!here> 사용 완료 : 윤재")

# asyncio.run(save_to_xml.main('TB24_200'))

# xml_to_dict.main()
# dict_to_db.main()

test.run()

