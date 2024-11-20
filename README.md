## KIPRIS 데이터 수집 및 분석 시스템

### 개요

이 프로젝트는 한국 특허정보검색시스템 (KIPRIS) Open API를 통해 특허, 상표, 디자인 데이터를 수집하고 분석하는 시스템입니다. 수집된 데이터는 MySQL 데이터베이스에 저장되며, Streamlit 기반의 대시보드를 통해 시각화 및 분석 결과를 확인할 수 있습니다. Airflow를 사용하여 데이터 수집 및 처리 과정을 자동화하고 스케줄링합니다. 또한, Prometheus와 Grafana를 통해 시스템 성능 및 API 호출 상태를 모니터링하여 안정적인 시스템 운영을 지원합니다.

### 주요 기능

* **데이터 수집:** KIPRIS Open API를 통해 특허, 상표, 디자인 데이터를 XML 형식으로 수집합니다.
* **데이터 변환:** 수집된 XML 데이터를 파싱하고, 데이터베이스에 저장하기 위한 SQL 쿼리로 변환합니다.
* **데이터베이스 저장:** 변환된 데이터를 MySQL 데이터베이스에 저장합니다.
* **데이터 분석 및 시각화:** Pandas, Plotly 등을 사용하여 데이터를 분석하고 Streamlit 대시보드를 통해 시각화합니다.
* **자동화 및 스케줄링:** Airflow를 사용하여 데이터 수집 및 처리 과정을 자동화하고 스케줄링합니다.
* **모니터링:** Prometheus 및 Grafana를 통해 시스템 성능 및 API 호출 상태를 모니터링합니다.

### 시스템 아키텍처

```
+-----------------+     +-----------------+     +-----------------+     +-----------------+     +-----------------+
| KIPRIS Open API |---->| Data Fetcher    |---->| XML Parser      |---->| SQL Converter   |---->| MySQL Database  |
+-----------------+     +-----------------+     +-----------------+     +-----------------+     +-----------------+
                                                                        ^
                                                                        |
                                                                        +------+---------------------+
                                                                        ^      |    Data Analyzer    |
                                                                        |      +---------------------+
                                                                        |                 |
                                                                        |                 V
                                    +-------------------+---------------+      +---------------------+
                                    | Prometheus        |  Metrics      |      | Streamlit Dashboard |
                                    +-------------------+---------------+      +---------------------+
                                                |                                         ^
                                                V                                         |
                                    +-------------------+---------------+      +----------------------+
                                    | Grafana           |  Dashboard    |      | flask Dashboard      |
                                    +-------------------+---------------+      +----------------------+
```

### 설치 및 실행 방법


- **Docker 컨테이너 실행 (개발 환경):**

```bash
./install_dev.sh
```

- **Docker 컨테이너 실행 (운영 환경):**

```bash
./install_public.sh
```
- **Airflow 초기화 및 실행:**
```bash
./run/airflow/init.sh # airflow 초기화
./run/airflow/server.sh # airflow 실행
```
- **데이터 수집 및 처리 (Airflow DAG 실행):**

```bash
airflow dags trigger all_task-1.0 # 전체 태스크 실행
airflow dags trigger except-task # xml 제외 전체 태스크 실행
```

- **Streamlit 대시보드 실행:**

```bash
./run/dashboard/all.sh
```

- **시스템 모니터링:** Prometheus 및 Grafana를 사용하여 시스템 및 API 호출 상태를 모니터링합니다. (자세한 설정 방법은 Prometheus 및 Grafana 문서 참조)


### 디렉토리 구조

```
├── src
│   ├── airflow
│   │   └── dag
│   │       ├── all_task.py  # Airflow DAG 정의 파일
│   │       └── all_task_except_xml.py  # XML 수집 제외 Airflow DAG 정의 파일
│   ├── bin
│   │   ├── save_to_xml.py      # XML 데이터 수집 모듈
│   │   ├── xml_to_sql.py      # XML to SQL 변환 모듈
│   │   └── sql_to_db          # SQL to Database 적재 모듈
│   │       ├── base.py
│   │       ├── ipc_cpc.py
│   │       └── priority.py
│   ├── dashboard
│   │   ├── flask
│   │   │   └── app.py         # Flask 웹 애플리케이션
│   │   └── streamlit
│   │       ├── app_pages     # Streamlit 페이지 모듈
│   │       │   ├── company_analyze.py
│   │       │   ├── company_data.py
│   │       │   ├── dashboard.py
│   │       │   ├── legal_status.py
│   │       │   └── report.py # report
│   │       ├── db_connection.py # db 연결 정보
│   │       └── main.py        # Streamlit 메인 애플리케이션
│   ├── db
│   │   └── mysql.py           # MySQL 데이터베이스 연동 모듈
│   ├── enum
│   │   ├── ApiType.py
│   │   ├── Config.py
│   │   ├── KiprisEntityType.py
│   │   └── TableName.py
│   ├── kipris
│   │   ├── core
│   │   │   ├── KiprisObject.py
│   │   │   ├── parsing
│   │   │   │   ├── KiprisApplicantInfoFetcher.py
│   │   │   │   ├── KiprisFetchData.py
│   │   │   │   └── KiprisParam.py
│   │   │   ├── prosess
│   │   │   │   └── KiprisXmlFileGenerator.py
│   │   │   └── upload
│   │   │       └── KiprisDataBatchUploader.py
│   │   ├── parsing
│   │   │   ├── fetcher
│   │   │   │   ├── KiprisDesignFetcher.py
│   │   │   │   ├── KiprisPatentFetcher.py
│   │   │   │   └── KiprisTrademarkFetcher.py
│   │   │   ├── xml
│   │   │   │   ├── KiprisXml.py
│   │   │   │   ├── KiprisXmlData.py
│   │   │   │   └── KiprisXmlDataGenerator.py
│   │   │   └── params # pram이 아니라 params 폴더명 오타
│   │   │       ├── KiprisDesignPram.py
│   │   │       ├── KiprisPatentParam.py
│   │       │       └── KiprisTrademarkParam.py
│   │   ├── convert
│   │   │   ├── cartridge
│   │   │   │   ├── KiprisDesignDataCartridge.py
│   │   │   │   ├── KiprisPatentDataCartridge.py
│   │   │   │   └── KiprisTrademarkDataCartridge.py
│   │   │   ├── converter
│   │   │   │   ├── KiprisDesignXmlToDictConverter.py
│   │   │   │   ├── KiprisPatentXmlToDictConverter.py
│   │   │   │   └── KiprisTrademarkXmlToDictConverter.py
│   │   │   └── mapper
│   │   │       ├── KiprisDesignXmlMapper.py
│   │   │       ├── KiprisIpcXmlMapper.py
│   │   │       ├── KiprisPatentXmlMapper.py
│   │   │       └── KiprisTrademarkXmlMapper.py
│   │   └── upload
│   │       └── uploader
│   │           ├── KiprisTB24DesignDataUploader.py
│   │           ├── KiprisTB24PatentDataUploader.py
│   │           └── KiprisTB24TrademarkDataUploader.py

│   └── util
│       ├── monitoring.py
│       └── util.py
├── main.py                   # 메인 실행 파일
├── debug.py                  # 디버깅용 스크립트
├── install_dev.sh             # 개발 환경 설치 스크립트
├── install_public.sh        # 운영 환경 설치 스크립트
├── run
│   ├── airflow
│   │   ├── init.sh           # Airflow 초기화 스크립트
│   │   ├── server.sh         # Airflow 서버 실행 스크립트
│   │   └── stop.sh           # Airflow 서버 중지 스크립트
│   ├── all_stop_server.sh # airflow, flask, streamlit 서버 중지
│   ├── dashboard
│   │   ├── all.sh            # 모든 대시보드 실행
│   │   ├── flask.sh          # Flask 대시보드 실행
│   │   ├── stop.sh           # 대시보드 중지 스크립트
│   │   └── streamlit.sh     # Streamlit 대시보드 실행
│   ├── save_to_xml           # XML 데이터 수집 스크립트
│   │   ├── company
│   │   │   ├── design.sh
│   │   │   ├── patent.sh
│   │   │   └── trademark.sh
│   │   └── university
│   │       ├── design.sh
│   │       ├── patent.sh
│   │       └── trademark.sh
│   ├── sql_to_db           # SQL to DB 스크립트
│   │   ├── base
│   │   │   ├── company
│   │   │   │   ├── design.sh
│   │   │   │   ├── patent.sh
│   │   │   │   └── trademark.sh
│   │   │   └── university
│   │   │       ├── design.sh
│   │   │       ├── patent.sh
│   │   │       └── trademark.sh
│   │   ├── ipc_cpc
│   │   │   ├── company
│   │   │   │   └── patent.sh
│   │   │   └── university
│   │   │       └── patent.sh
│   │   └── priority
│   │       ├── company
│   │       │   ├── design.sh
│   │       │   └── trademark.sh
│   │       └── university
│   │           ├── design.sh
│   │           └── trademark.sh

│   ├── test.sh                # 테스트 스크립트
│   └── xml_to_sql           # XML to SQL 스크립트
│       ├── company
│       │   ├── design.sh
│       │   ├── patent.sh
│       │   └── trademark.sh
│       └── university
│           ├── design.sh
│           ├── patent.sh
│           └── trademark.sh
├── test                      # 테스트 디렉토리
│   ├── all_conn
│   │   └── all_conn.py
│   ├── blocked_users
│   │   └── blocked_users.py
│   ├── count.py
│   ├── kipris
│   │   ├── convert
│   │   │   ├── dict_to_sql.py
│   │   │   └── dict_to_sql_sub.py
│   │   ├── parsing
│   │   │   ├── applicant_info_fetcher.py
│   │   │   ├── fetcher.py
│   │   │   ├── fetcher_data.py
│   │   │   └── param.py
│   │   └── upload
│   │       └── uploader.py
│   ├── prometheus
│   │   └── prometheus.py
│   ├── save_to_db
│   │   └── sql_to_db.py
│   └── save_to_xml          
│       ├── api_modules
│       │    ├── biz_api.py  
│       │    ├── design_api.py  
│       │    ├── patent_api.py  
│       │    └── trademark_api.py  
│       └── save_to_xml.py

└── README.md

```

### 주요 모듈 설명

* **`src/kipris`:** KIPRIS Open API 연동 및 데이터 처리 관련 모듈들을 포함합니다.
    * **`core`:** 핵심 기능 구현 (파라미터 처리, 데이터 변환 등)
    * **`parsing`:** API 데이터 파싱 및 XML 생성
    * **`convert`:** XML 데이터를 SQL 쿼리로 변환
    * **`upload`:** 데이터베이스 업로드 기능
* **`src/bin`:**  데이터 수집, 변환, 적재를 위한 실행 스크립트들을 포함합니다.
* **`src/dashboard`:**  데이터 시각화 및 분석 대시보드 관련 모듈들을 포함합니다.
* **`src/db`:** 데이터베이스 연동 모듈
* **`src/enum`:**  Enum 클래스 정의
* **`src/test`:** 테스트 코드
* **`src/util`:**  유틸리티 함수 모듈 (로깅, 시간 측정 등)



### 라이선스

MIT License

