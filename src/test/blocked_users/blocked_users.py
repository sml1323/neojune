import os
import lxml.etree as etree
from ...util import util
from ...kipris.core.parsing.KiprisApplicantInfoFetcher import KiprisApplicantInfoFetcher

def __is_blocked_users(content: str=""):
    if content == "":
        return False

    root:etree = etree.fromstring(content.encode("utf-8"))
    result_msg = root.find(".//resultMsg").text

    return result_msg == "Blocked users."
    
def throw_error_if_blocked_users(content: str=""):
    if __is_blocked_users(content):
        raise Exception("User is blocked.")
     

def test(xml:str):
    try:
        throw_error_if_blocked_users(xml)
        print("문제 없음")
    except Exception as e:
        print(e)

def main():
    dir_path = f"{os.path.dirname(os.path.abspath(__file__))}"
    one_xml = util.get_file(f"{dir_path}/1.xml")
    blocked_users_xml = util.get_file(f"{dir_path}/blocked_users.xml")
    test(one_xml)
    test(blocked_users_xml)