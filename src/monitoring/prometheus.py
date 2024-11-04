
from prometheus_client import Counter, Summary, Histogram

# API 호출 횟수와 시간 측정용 메트릭 정의
API_CALL_COUNT = Counter('api_calls_total', 'Total number of API calls')
# API_RESPONSE_TIME = Summary('api_response_processing_seconds', 'Time taken for API requests and responses')
API_RESPONSE_TIME= Histogram(
    'api_response_time_seconds',
    'Time taken for API requests',
    buckets=[0.1, 0.5, 1, 2, 3, 5, 10]  # 사용자 정의 버킷
)

DB_SAVE_TIME = Summary(
    'db_save_time_seconds', 
    'Time taken to save data to DB', 
    ['table_name']
)
