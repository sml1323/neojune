import asyncio, aiohttp
from .KiprisFetchData import KiprisFetchData
from .KiprisApplicantInfoFetcher import KiprisApplicantInfoFetcher
from .KiprisParams import KiprisParams





class KiprisFetcher:
    def __init__(self, url:str='', params:list[KiprisParams]=KiprisParams()):
        self.url = url
        self.params = params

    async def __task(self, semaphore, param:KiprisParams):
        async with semaphore:
            info = KiprisApplicantInfoFetcher(self.url, param)
            return await info.get_info()
        

    async def get_infos(self) -> list[KiprisFetchData]:
        semaphore = asyncio.Semaphore(50)
        tasks = []
        for param in self.params:
            tasks.append(asyncio.create_task(self.__task(semaphore, param)))
        return await asyncio.gather(*tasks)
    
    def __is_not_first_kipris_prams(self, params_list):
        return not isinstance(params_list[0], KiprisParams)
    
    def set_params(self, params_list:list[str|int], ParamType:KiprisParams=KiprisParams):
        if(self.__is_not_first_kipris_prams(params_list)):
            res = []
            for params in params_list:
                res.append(ParamType(params))
            self.params = res

async def main():
    applicant = "120140558200"
    kipris_applicant_info_fetcher = KiprisFetcher()
    async with aiohttp.ClientSession() as session:
        result = await kipris_applicant_info_fetcher.get_info(applicant, session)

if __name__ == "__main__":
    asyncio.run(main())
