import asyncio, aiohttp
from ..kipris_xml.KiprisFetchData import KiprisFetchData
from .KiprisApplicantInfoFetcher import KiprisApplicantInfoFetcher
from .core.KiprisParams import KiprisParams





class KiprisFetcher:
    def __init__(self, url:str, params:list[KiprisParams]):
        self.url = url
        self.params = params

    async def __task(self, semaphore, param:KiprisParams):
        async with semaphore:
            info = KiprisApplicantInfoFetcher(self.url, param)
            return await info.get_info()
        

    async def get_fetch_app_infos(self) -> list[KiprisFetchData]:
        semaphore = asyncio.Semaphore(50)
        tasks = []
        for param in self.params:
            tasks.append(asyncio.create_task(self.__task(semaphore, param)))
        return await asyncio.gather(*tasks)

async def main():
    applicant = "120140558200"
    kipris_applicant_info_fetcher = KiprisFetcher()
    async with aiohttp.ClientSession() as session:
        result = await kipris_applicant_info_fetcher.get_info(applicant, session)

if __name__ == "__main__":
    asyncio.run(main())
