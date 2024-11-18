import asyncio, aiohttp
from .KiprisFetchData import KiprisFetchData
from .KiprisApplicantInfoFetcher import KiprisApplicantInfoFetcher
from .KiprisParam import KiprisParam
from tqdm import tqdm
from ....util.util import yappi_profiler
from ....test.prometheus.prometheus import PrometheusDashboard

semaphore = asyncio.Semaphore(20)

class KiprisFetcher:
    def __init__(self, url:str='', params:list[KiprisParam]=[KiprisParam()]):
        self.url = url
        self.params = params

    async def __task(self, param: KiprisParam, session: aiohttp.ClientSession):
        info = KiprisApplicantInfoFetcher(self.url, param)
        # self.prometheus.api_counter_plus()
        result = await info.get_info(session)  # session 전달
        # self.prometheus.api_response_time()
        return result
    
    async def get_infos(self, file_name: str = "default.prof", org_type:str = 'comp') -> list:
        # self.prometheus = PrometheusDashboard(org_type=org_type, service_type=file_name)
        # 여기서 yappi_profiler를 동적으로 적용하여 호출
        base_path = "res/log"
        profiled_get_infos = yappi_profiler(f'{base_path}/{file_name}')(self.__get_infos)
        return await profiled_get_infos()

    # async def _get_infos(self) -> list:
    #     tasks = []
    #     for param in tqdm(self.params):
    #         task = self.__task(param)
    #         tasks.append(task)
    #     return await asyncio.gather(*tasks)

    async def __get_infos(self) -> list:
        tasks = []
        async with aiohttp.ClientSession() as session: 
            for param in self.params:
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
