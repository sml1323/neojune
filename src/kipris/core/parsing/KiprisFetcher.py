import asyncio, aiohttp
from .KiprisFetchData import KiprisFetchData
from .KiprisApplicantInfoFetcher import KiprisApplicantInfoFetcher
from .KiprisParam import KiprisParam
from tqdm import tqdm
from ....enum.Config import Config
from ....util import util
from ....test.prometheus.prometheus import PrometheusDashboard
import random
from aiolimiter import AsyncLimiter 



semaphore = asyncio.Semaphore(45)

rate_limiter = AsyncLimiter(max_rate=40, time_period=1)

class KiprisFetcher:
    def __init__(self, url:str='', params:list[KiprisParam]=[KiprisParam()]):
        self.url = url
        self.params = params
        self.prometheus:PrometheusDashboard = None

    async def __task(self, param: KiprisParam, session: aiohttp.ClientSession):
        # Prometheus 없이도 실행 가능하도록 처리
        info = KiprisApplicantInfoFetcher(self.url, param)
        result = await info.get_info(session, self.prometheus)

        if self.prometheus:  # Prometheus가 연결되었을 때만 시간 기록
            self.prometheus.api_total_time()

        return result

    async def get_infos(self, file_name: str = "default.prof", org_type: str = 'comp') -> list:
        self.prometheus = PrometheusDashboard(org_type=org_type, service_type=file_name)

        # 프로파일링 적용
        base_path = f"{Config.OUTPUT_PATH.value}/{util.get_timestamp()}/log"
        profiled_get_infos = util.yappi_profiler(f'{base_path}/{file_name}')(self.__get_infos)
        return await profiled_get_infos()


    async def __get_infos(self) -> list:
        tasks = []
        async with aiohttp.ClientSession() as session: 
            for param in self.params:
                await asyncio.sleep(0.02)
                task = asyncio.create_task(self.__task(param, session)) 
                tasks.append(task)
            return await asyncio.gather(*tasks)
    
    def set_params(self, params_list:list[str|int], ParamType:KiprisParam=KiprisParam):
        res = []
        for params in params_list:
            res.append(ParamType(*params))
        self.params = res

async def main():
    applicant = "120140558200"
    kipris_applicant_info_fetcher = KiprisFetcher()
    async with aiohttp.ClientSession() as session:
        result = await kipris_applicant_info_fetcher.get_info(applicant, session)

if __name__ == "__main__":
    asyncio.run(main())
