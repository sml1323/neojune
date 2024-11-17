import argparse
import asyncio
from src.bin import save_to_xml, xml_to_sql
from src.util import util

from src.test import test
test.run()
exit(0)


# 각 모듈의 작업 함수 딕셔너리
module_tasks = {
    'save_to_xml': {
        'company_patent': save_to_xml.run_company_patent,
        'company_design': save_to_xml.run_company_design,
        'company_trademark': save_to_xml.run_company_trademark,
        'university_patent': save_to_xml.run_university_patent,
        'university_design': save_to_xml.run_university_design,
        'university_trademark': save_to_xml.run_university_trademark,
    },
    'xml_to_sql': {
        'company_design': xml_to_sql.run_company_design,
        'company_patent': xml_to_sql.run_company_patent,
        'company_trademark': xml_to_sql.run_company_trademark,
        'university_design': xml_to_sql.run_university_design,
        'university_patent': xml_to_sql.run_university_patent,
        'university_trademark': xml_to_sql.run_university_trademark,
    }
}

async def main():
    parser = argparse.ArgumentParser(description="Run specific module tasks")
    parser.add_argument('--run', nargs='+', help="Specify module and tasks, e.g., 'save_to_xml company_patent'")
    args = parser.parse_args()

    if not args.run or len(args.run) < 2:
        print("Usage: python script_name.py --run <module> <task1> <task2> ...")
        return

    module = args.run[0]
    tasks = args.run[1:]

    if module not in module_tasks:
        print(f"Error: Unknown module '{module}'")
        return

    # 작업 분류 및 실행
    if module == 'save_to_xml':  # 비동기 작업 처리
        async_jobs = []
        for task in tasks:
            if task in module_tasks[module]:
                async_jobs.append(module_tasks[module][task]())
            else:
                print(f"Warning: Task '{task}' not found in module '{module}'")
        
        async def inner():
            for job in async_jobs:
                await job
    
        # await util.send_slack_message("neojune", inner)
        await inner()
        

    elif module == 'xml_to_sql':  # 동기 작업 처리
        for task in tasks:
            if task in module_tasks[module]:
                module_tasks[module][task]()
            else:
                print(f"Warning: Task '{task}' not found in module '{module}'")

# if __name__ == '__main__':
#     asyncio.run(main())
