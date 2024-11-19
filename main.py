import sys
import asyncio
from src.bin import save_to_xml, xml_to_sql, dict_to_sql_sub
from src.bin.sql_to_db import base, ipc_cpc, priority
from src.util import util


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
        'company_patent': xml_to_sql.run_company_patent,
        'company_design': xml_to_sql.run_company_design,
        'company_trademark': xml_to_sql.run_company_trademark,
        'university_patent': xml_to_sql.run_university_patent,
        'university_design': xml_to_sql.run_university_design,
        'university_trademark': xml_to_sql.run_university_trademark,
    },
    'dict_to_sql_sub': {
        'company_patent': dict_to_sql_sub.run_company_patent,
        'company_design': dict_to_sql_sub.run_company_design,
        'company_trademark': dict_to_sql_sub.run_company_trademark,
        'university_patent': dict_to_sql_sub.run_university_patent,
        'university_design': dict_to_sql_sub.run_university_design,
        'university_trademark': dict_to_sql_sub.run_university_trademark,
    },
    'sql_to_db': {
        'base': {
            'company_patent': base.run_company_design,
            'company_design': base.run_company_patent,
            'company_trademark': base.run_company_trademark,
            'university_patent': base.run_university_design,
            'university_design': base.run_university_patent,
            'university_trademark': base.run_university_trademark,
        },
        'ipc_cpc': {
            'company_patent': ipc_cpc.run_company_patent,
            'university_patent': ipc_cpc.run_university_patent,
        },
        'priority': {
            'company_design': priority.run_company_design,
            'company_trademark': priority.run_company_trademark,
            'university_design': priority.run_university_design,
            'university_trademark': priority.run_university_trademark,
        },
    }
}

# 재귀적으로 딕셔너리 탐색
async def execute_task(task_tree, keys):
    if not keys:  # keys가 비어 있으면
        if callable(task_tree):  # 현재 값이 함수면 실행
            # 함수가 비동기 함수라면 await
            if asyncio.iscoroutinefunction(task_tree):
                await task_tree()
            else:
                task_tree()
        else:
            print("Error: Task is not executable.")
        return

    key = keys.pop(0)  # 키를 하나 꺼내고
    if key in task_tree:  # 해당 키가 트리에 있으면
        await execute_task(task_tree[key], keys)
    else:
        print(f"Error: Key '{key}' not found.")

async def main():
    args = sys.argv[1:]  # 실행 시 전달된 인자 목록
    if not args:
        print("Usage: python main.py <key1> <key2> ...")
        return

    module = args[0]  # 첫 번째 값은 모듈 이름
    tasks = args[1:]  # 나머지 값들은 태스크 이름들

    if module not in module_tasks:
        print(f"Error: Module '{module}' not found.")
        return

    await execute_task(module_tasks[module], tasks)

if __name__ == "__main__":
    asyncio.run(main())
