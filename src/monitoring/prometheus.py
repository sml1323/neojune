
from prometheus_client import Counter, Summary

# API 호출 횟수와 시간 측정용 메트릭 정의
API_CALL_COUNT = Counter('api_calls_total', 'Total number of API calls')
API_RESPONSE_TIME = Summary('api_response_processing_seconds', 'Time taken for API requests and responses')
