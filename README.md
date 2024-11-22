## KIPRIS 데이터 수집 및 분석 시스템


### 라이선스 및 사용 정책

이 프로젝트는 **팀 포트폴리오** 용도로 제작되었습니다.  
저작권은 프로젝트에 참여한 팀원 전원에게 귀속되며, 아래와 같은 조건에 따라 사용이 제한됩니다.

#### 허용되는 활동  
- 학습 및 연구 목적으로의 사용  
- 비상업적인 용도로의 활용  

#### 금지되는 활동  
- 팀원을 제외한 소스 코드 배포  
- 팀원을 제외한 상업적 이용  
- 팀원을 제외한 무단 수정 및 재배포  
- 프로그램 및 소스 코드 내 저작권 표시 제거  

---

### 개요

이 프로젝트는 한국 특허정보검색시스템 (KIPRIS) Open API를 통해 특허, 상표, 디자인 데이터를 수집하고 분석하는 시스템입니다. 수집된 데이터는 MySQL 데이터베이스에 저장되며, Streamlit 기반의 대시보드를 통해 시각화 및 분석 결과를 확인할 수 있습니다. Airflow를 사용하여 데이터 수집 및 처리 과정을 자동화하고 스케줄링합니다. 또한, Prometheus와 Grafana를 통해 시스템 성능 및 API 호출 상태를 모니터링하여 안정적인 시스템 운영을 지원합니다.

---

### 주요 기능

* **데이터 수집:** KIPRIS Open API를 통해 특허, 상표, 디자인 데이터를 XML 형식으로 수집합니다.
* **데이터 변환:** 수집된 XML 데이터를 파싱하고, 데이터베이스에 저장하기 위한 SQL 쿼리로 변환합니다.
* **데이터베이스 저장:** 변환된 데이터를 MySQL 데이터베이스에 저장합니다.
* **데이터 분석 및 시각화:** Pandas, Plotly 등을 사용하여 데이터를 분석하고 Streamlit 대시보드를 통해 시각화합니다.
* **자동화 및 스케줄링:** Airflow를 사용하여 데이터 수집 및 처리 과정을 자동화하고 스케줄링합니다.
* **모니터링:** Prometheus 및 Grafana를 통해 시스템 성능 및 API 호출 상태를 모니터링합니다.

---

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

---

### 기술 스택

* Python
* MySQL
* Docker
* Airflow
* Prometheus
* Grafana
* Flask
* Streamlit
* KIPRIS Open API

---


### `.env` 파일 생성 및 설정

1. **`.env` 파일 생성:** 프로젝트 루트 디렉토리에 `.env` 파일을 생성합니다. (`.env.example` 파일을 복사해서 사용하는 것이 좋습니다.)

2. **환경 변수 설정:** `.env` 파일에 다음과 같은 형식으로 환경 변수를 설정합니다.

   ```
   변수이름=값
   ```

   예시:

   ```
   DB_HOST=kt2.elementsoft.biz
   DB_USER=kipris
   DB_PASSWORD=비번
   DB_NAME=kipris
   DB_PORT=13306
   SERVICE_KEY=YOUR_KIPRIS_SERVICE_KEY  # 실제 서비스 키로 변경
   OUTPUT_PATH=app/res/output
   PUSH_GATEWAY_ADDRESS=54.180.253.90:9091 # prometheus push gateway 주소
   ```

   * **`DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`, `DB_PORT`**: MySQL 데이터베이스 연결 정보입니다. 실제 사용하는 데이터베이스 정보로 변경해야 합니다.
   * **`SERVICE_KEY`**: KIPRIS Open API에 접근하기 위한 서비스 키입니다.  KIPRIS에서 발급받은 서비스 키로 변경해야 합니다.
   * **`OUTPUT_PATH`**:  데이터 수집 결과물 (XML, SQL 파일) 도커 오퍼레이터 안에서 저장될 경로입니다. 로컬 저장장소와 연결됩니다.
   * **`PUSH_GATEWAY_ADDRESS`**: Prometheus Pushgateway의 주소입니다.  Prometheus 설정에 따라 변경해야 합니다.  
        **실행하는 서버의 주소를 입력 해야합니다** **`매우 중요!`**

3. **`.gitignore`에 `.env` 추가:** `.env` 파일에는 중요한 정보 (데이터베이스 비밀번호, API 키 등)가 포함될 수 있으므로,  `.gitignore` 파일에 `.env`를 추가하여 Git 저장소에 포함되지 않도록 해야 합니다.

---


### 설치 및 실행 방법


- **Docker 컨테이너 실행 (개발 환경):**

```bash
./install_dev.sh
```

- **Docker 컨테이너 실행 (운영 환경):**

```bash
./install_public.sh
```
- `src/install/public/airflow/dags/kipris_daily.py` 에서
```
# 호스트에 XML 파일이 저장될 경로
host_output_path = "/home/ubuntu/app/res/output"
```
디렉토리를 만들어 주고 경로를 수정해야 합니다.  
이 폴더는 DockerOperator 이미지 경로에 마운트되며, 날짜별로 다음 파일이 생성  
- XML파일
- SQL 파일
- Log 파일
---

**Airflow DAG 확인**

- `src/install/airflow/dags/kipris_daily.py` 에서 스케쥴링, 이미지 이름 등 확인하고 수정
- 8081 포트(해당 서버 public ip)로 접속하여 kipris_daily DAG를 확인
- {public ip}:8081

#### 실행 스크립트

* **`run/dashboard/start.sh`**: Airflow, Grafana, Prometheus, Pushgateway, Flask, Streamlit 대시보드를 모두 실행합니다.
* **`run/dashboard/start_view.sh`**: Flask, Streamlit 대시보드만 실행합니다.
* **`run/dashboard/stop.sh`**:  실행 중인 모든 대시보드 및 관련 서비스를 중지합니다.
* **`run/dashboard/stop_view.sh`**: 실행 중인 Flask, Streamlit 대시보드만 중지합니다.
* **`run/dashboard/*/{start|stop}.sh`**: 각 대시보드 서비스를 개별적으로 실행하거나 중지하는 스크립트입니다. (예: `run/dashboard/airflow/start.sh`)
* **`run/all_stop_server.sh`**: airflow, flask, streamlit 서버를 중지합니다.

---

#### 대시보드 사용

* **Streamlit 대시보드:** `http://localhost:8501`
* **Flask 대시보드:** `http://localhost:5000`
* **Grafana:** `http://localhost:3000`
* **Prometheus:** `http://localhost:9090`
* **Pushgateway:** `http://localhost:9091`
* **Airflow:** `http://localhost:8080`

---

### 주요 디렉토리 및 파일 설명

* `src/bin`: 데이터 수집, 처리, 변환, 적재 관련 스크립트
* `src/db`: 데이터베이스 연결 및 관리 모듈
* `src/enum`:  프로젝트에서 사용되는 열거형 (Enum) 정의
* `src/kipris`: KIPRIS Open API 연동 및 데이터 처리 모듈
* `src/test`: 테스트 코드 및 예제
* `src/util`: 유틸리티 함수 및 모듈
* `src/dashboard/flask`:  Flask 기반 대시보드 애플리케이션
* `src/dashboard/streamlit`:  Streamlit 기반 대시보드 애플리케이션
* `.env`: 환경 변수 설정 파일 (예시: `.env.example`)

---

### 디렉토리 구조 및 실행 파일 설명

```
.
├── debug.py
├── debug.sh                      # 디버깅용 스크립트 실행
├── Dockerfile
├── install_dev.sh                # 개발 환경용 Docker 이미지 빌드 및 컨테이너 실행
├── install_public.sh             # 운영 환경 설치 스크립트 (Airflow, Prometheus 설정 및 Docker 이미지 빌드)
├── main.py
├── main.sh                       # main.py 실행 스크립트
├── README.md
├── res
│   ├── output
│   │   └── ...
│   └── url
│       ├── list_design.json
│       ├── list_patent.json
│       ├── list_trademark.json
│       ├── list_univ_design.json
│       ├── list_univ_patent.json
│       └── list_univ_trademark.json
├── run                           # 실행 스크립트 모음
│   ├── all_stop_server.sh        # Airflow, Flask, Streamlit 서버 중지
│   ├── dashboard                 # 대시보드 관련 스크립트
│   │   ├── airflow
│   │   │   ├── start.sh        # Airflow 웹서버 및 스케줄러 실행
│   │   │   └── stop.sh         # Airflow 웹서버 및 스케줄러 중지
│   │   ├── flask               # Flask 관련 스크립트
│   │   │   ├── app.py
│   │   │   ├── start.sh        # Flask 애플리케이션 실행
│   │   │   ├── stop.sh         # Flask 애플리케이션 중지
│   │   │   └── templates       # Flask 템플릿 파일
│   │   │       ├── company.html
│   │   │       ├── index.html
│   │   │       └── index_uni.html
│   │   ├── grafana
│   │   │   ├── start.sh        # Grafana 서버 실행
│   │   │   └── stop.sh         # Grafana 서버 중지
│   │   ├── prometheus
│   │   │   ├── start.sh        # Prometheus 서버 실행
│   │   │   └── stop.sh         # Prometheus 서버 중지
│   │   ├── pushgateway
│   │   │   ├── start.sh        # Pushgateway 실행
│   │   │   └── stop.sh         # Pushgateway 중지
│   │   ├── start.sh            # 모든 대시보드 서비스 실행
│   │   ├── start_view.sh       # Flask 및 Streamlit 대시보드만 실행
│   │   ├── stop.sh             # 모든 대시보드 서비스 중지
│   │   └── stop_view.sh        # Flask 및 Streamlit 대시보드만 중지
│   ├── save_to_xml             # XML 저장 스크립트
│   │   ├── company
│   │   │   ├── design.sh      # 기업 디자인 데이터를 XML로 저장
│   │   │   ├── patent.sh      # 기업 특허 데이터를 XML로 저장
│   │   │   └── trademark.sh   # 기업 상표 데이터를 XML로 저장
│   │   └── university
│   │       ├── design.sh      # 대학 디자인 데이터를 XML로 저장
│   │       ├── patent.sh      # 대학 특허 데이터를 XML로 저장
│   │       └── trademark.sh   # 대학 상표 데이터를 XML로 저장
│   ├── sql_to_db              # 데이터베이스 적재 스크립트
│   │   ├── base
│   │   │   ├── company
│   │   │   │   ├── design.sh    # 기업 디자인 데이터를 DB에 적재
│   │   │   │   ├── patent.sh    # 기업 특허 데이터를 DB에 적재
│   │   │   │   └── trademark.sh # 기업 상표 데이터를 DB에 적재
│   │   │   └── university
│   │   │       ├── design.sh    # 대학 디자인 데이터를 DB에 적재
│   │   │       ├── patent.sh    # 대학 특허 데이터를 DB에 적재
│   │   │       └── trademark.sh # 대학 상표 데이터를 DB에 적재
│   │   ├── ipc_cpc
│   │   │   ├── company
│   │   │   │   └── patent.sh  # 기업 특허 IPC/CPC 데이터를 DB에 적재
│   │   │   └── university
│   │   │       └── patent.sh  # 대학 특허 IPC/CPC 데이터를 DB에 적재
│   │   └── priority
│   │       ├── company
│   │       │   ├── design.sh  # 기업 디자인 우선권 데이터를 DB에 적재
│   │       │   └── trademark.sh # 기업 상표 우선권 데이터를 DB에 적재
│   │       └── university
│   │           ├── design.sh  # 대학 디자인 우선권 데이터를 DB에 적재
│   │           └── trademark.sh # 대학 상표 우선권 데이터를 DB에 적재
│   └── test.sh                  # 테스트 스크립트 실행
└── src                           # 소스 코드 디렉토리
    ├── bin                       # 실행 가능한 스크립트
    │   ├── dict_to_sql_sub.py
    │   ├── save_to_xml.py
    │   ├── sql_to_db
    │   │   ├── base.py
    │   │   ├── ipc_cpc.py
    │   │   └── priority.py
    │   └── xml_to_sql.py
    ├── dashboard
    │   ├── flask
    │   │   ├── app.py
    │   │   └── ...
    │   └── streamlit
    │       ├── app_pages
    │       │   ├── company_analyze.py
    │       │   ├── company_data.py
    │       │   ├── dashboard.py
    │       │   ├── legal_status.py
    │       │   ├── report.py
    │       │   ├── university_analyze.py
    │       │   └── university_data.py
    │       ├── db_connection.py
    │       └── main.py
    │
    ├── db
    │   └── mysql.py
    ├── enum
    │   ├── ApiType.py
    │   ├── Config.py
    │   ├── KiprisEntityType.py
    │   └── TableName.py
    ├── install
    │   ├── dev
    │   │   ├── Dockerfile
    │   │   ├── setup.sh
    │   │   └── setup
    │   │       ├── airflow
    │   │       │   └── ...
    │   │       ├── grafana
    │   │       │   └── ...
    │   │       └── prometheus
    │   │           └── ...
    │   └── public
    │       ├── airflow
    │       │   └── ...
    │       └── prometheus
    │           └── ...
    ├── kipris
    │   ├── convert
    │   │   ├── cartridge
    │   │   │   └── ...
    │   │   ├── converter
    │   │   │   └── ...
    │   │   └── mapper
    │   │       └── ...
    │   ├── core
    │   │   ├── KiprisObject.py
    │   │   ├── KiprisParam.py
    │   │   ├── convert
    │   │   │   └── ...
    │   │   ├── parsing
    │   │   │   └── ...
    │   │   ├── prosess
    │   │   │   └── ...
    │   │   └── upload
    │   │       └── ...

    │   ├── parsing
    │   │   ├── KiprisParam.py
    │   │   ├── fetcher
    │   │   │   └── ...
    │   │   ├── params
    │   │   │   └── ...
    │   │   └── xml
    │   │       └── ...
    │   ├── prosess
    │   │   └── xml_file_generator
    │   │       └── ...
    │   └── upload
    │       └── uploader
    │           └── ...

    ├── test
    │   ├── all_conn
    │   │   └── ...
    │   ├── blocked_users
    │   │   └── ...
    │   ├── kipris
    │   │   └── ...
    │   ├── prometheus
    │   │   └── ...
    │   ├── save_to_db
    │   │   └── ...
    │   ├── save_to_xml
    │   │   └── ...
    │   └── test.py
    └── util
        ├── monitoring.py
        └── util.py


```

---

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

---


### 라이선스 및 사용 정책

이 프로젝트는 **팀 포트폴리오** 용도로 제작되었습니다.  
저작권은 프로젝트에 참여한 팀원 전원에게 귀속되며, 아래와 같은 조건에 따라 사용이 제한됩니다.

#### 허용되는 활동  
- 학습 및 연구 목적으로의 사용  
- 비상업적인 용도로의 활용  

#### 금지되는 활동  
- 팀원을 제외한 소스 코드 배포  
- 팀원을 제외한 상업적 이용  
- 팀원을 제외한 무단 수정 및 재배포  
- 프로그램 및 소스 코드 내 저작권 표시 제거  

