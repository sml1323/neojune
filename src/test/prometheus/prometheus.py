import os
import time

from prometheus_client import CollectorRegistry, Gauge, push_to_gateway, Counter


class PrometheusDashboard:
    def __init__(self, org_type, service_type) -> None:
        self.registry = CollectorRegistry()
        self.org_type = org_type
        self.service_type = service_type
        self.address = os.getenv('PUSH_GATEWAY_ADDRESS')
        
        self.base_txt = f'{self.org_type}_{self.service_type}'
        self.api_counter = Counter(f'{self.base_txt}_api_requests_total', 'API 호출 카운터', registry=self.registry)
        self.job_duration = Gauge(f'{self.base_txt}_duration', '호출 건당 작업 소요 시간', registry=self.registry)
        self.total_time = Gauge(f'{self.base_txt}_tital_time', '총 작업 소요시간', registry=self.registry)

    def api_counter_plus(self) -> None:
        self.starttime = time.time()
        self.api_counter.inc()
        self.__push_to_gateway()

    def api_response_time(self) -> None:
        self.endtime = time.time()
        self.job_duration.set(self.endtime - self.starttime)
        self.__push_to_gateway()

    def __push_to_gateway(self) -> None:
        push_to_gateway(self.address, job=f'{self.org_type}_{self.service_type}_api_job', registry=self.registry)

