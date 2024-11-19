import os
import time

from prometheus_client import CollectorRegistry, Gauge, push_to_gateway, Counter


class PrometheusDashboard:
    """
    Prometheus 대시보드를 위한 클래스.

    이 클래스는 Prometheus 메트릭을 수집하고, API 호출에 대한 카운터 및 작업 소요 시간을 기록합니다.
    """
    def __init__(self, org_type, service_type) -> None:
        """
        클래스 초기화.

        :param org_type: 조직 유형
        :param service_type: 서비스 유형
        """
        self.registry = CollectorRegistry()
        self.org_type = org_type
        self.service_type = service_type
        self.address = os.getenv('PUSH_GATEWAY_ADDRESS')
        self.total_starttime = time.time()

        self.base_txt = f'{self.org_type}_{self.service_type}'
        self.api_counter = Counter(f'{self.base_txt}_api_requests_total', 'API 호출 카운터', registry=self.registry)
        self.job_duration = Gauge(f'{self.base_txt}_duration', '호출 건당 작업 소요 시간', registry=self.registry)
        self.total_time = Gauge(f'{self.base_txt}_total_time', '총 작업 소요시간', registry=self.registry)

    def api_counter_plus(self) -> None:
        """
        API 호출 카운터를 증가시키고, 현재 작업의 시작 시간을 기록합니다.
        """
        self.starttime = time.time()
        self.api_counter.inc()
        self.__push_to_gateway()

    def api_response_time(self) -> None:
        """
        현재 작업의 소요 시간을 기록하고, 메트릭을 Push Gateway에 전송합니다.
        """
        endtime = time.time()
        self.job_duration.set(endtime - self.starttime)
        self.__push_to_gateway()

    def api_total_time(self) -> None:
        """
        전체 작업의 소요 시간을 기록하고, 메트릭을 Push Gateway에 전송합니다.
        """
        self.total_endtime = time.time()
        self.total_time.set(self.total_endtime - self.total_starttime)
        self.__push_to_gateway()

    def __push_to_gateway(self) -> None:
        """
        수집된 메트릭을 Push Gateway에 전송합니다.
        """
        push_to_gateway(self.address, job=f'{self.org_type}_{self.service_type}_api_job', registry=self.registry)

