from prometheus_client import CollectorRegistry, Gauge, push_to_gateway, Counter
import time
from random import randint


class PrometheusDashboard:
    def __init__(self, org_type, service_type) -> None:
        self.registry = CollectorRegistry()
        self.org_type = org_type
        self.service_type = service_type
        self.address = '54.180.253.90:9091'
        
        self.base_txt = f'{self.org_type}_{self.service_type}'
        self.api_counter = Counter(f'{self.base_txt}_api_requests_total', 'API 호출 카운터', registry=self.registry)
        self.job_duration = Gauge(f'{self.base_txt}_duration', '호출 건당 작업 소요 시간', registry=self.registry)
        self.total_time = Gauge(f'{self.base_txt}_tital_time', '총 작업 소요시간', registry=self.registry)

    def monitoring(self):
        starttime = time.time()
        self.api_counter.inc()
        endtime = time.time()
        self.job_duration.set(endtime - starttime)
        print(f"API 호출 카운터: {self.api_counter._value.get()}, 작업 소요 시간: {endtime - starttime}")
    
        self._push_to_gateway()
    
    def _push_to_gateway(self):
        push_to_gateway(self.address, job=f'{self.org_type}_{self.service_type}_api_job', registry=self.registry)

class_list = []

for i in ['comp', 'univ']:
    for j in ['patent', 'design', 'trademark']:
        p = PrometheusDashboard(i, j)
        class_list.append(p)



while True:
    for p in class_list:
        p.monitoring()
    # break

        
