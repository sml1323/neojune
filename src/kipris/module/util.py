def get_kipris_api_url(service_name):
    """KIPRIS Open API URL을 반환합니다.

    Args:
        service_name (str): 사용할 서비스 이름

    Returns:
        str: KIPRIS Open API URL
    """
    return f"http://plus.kipris.or.kr/kipo-api/kipi/{service_name}/getAdvancedSearch"
