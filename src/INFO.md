## KIPRIS 데이터 수집 및 처리 모듈 매뉴얼

### 개요

이 Python 모듈은 KIPRIS Open API를 통해 특허, 디자인, 상표 데이터를 효율적으로 수집, 처리, 변환, 저장하고 데이터베이스에 업로드하는 기능을 제공합니다. 비동기 처리를 통해 대량의 데이터를 빠르게 가져오고, 표준화된 형식으로 변환하여 데이터 분석에 활용할 수 있도록 합니다.

### 모듈 구조

```
.
├── db
│   └── mysql.py
└── kipris
    ├── core
    │   ├── KiprisObject.py
    │   ├── convert
    │   │   ├── KiprisMapping.py
    │   │   └── KiprisXmlToDictConverter.py
    │   ├── parsing
    │   │   ├── KiprisApplicantInfoFetcher.py
    │   │   ├── KiprisFetchData.py
    │   │   ├── KiprisFetcher.py
    │   │   └── KiprisParams.py
    │   └── upload
    │       └── KiprisDataBatchUploader.py
    ├── convert
    │   ├── converter
    │   │   ├── KiprisDesignXmlToDictConverter.py
    │   │   ├── KiprisPatentXmlToDictConverter.py
    │   │   └── KiprisTrademarkXmlToDictConverter.py
    │   └── mapping
    │       ├── DesignKiprisMapping.py
    │       ├── PatentKiprisMapping.py
    │       └── TrademarkKiprisMapping.py
    ├── parsing
    │   ├── fetcher
    │   │   ├── KiprisDesignFetcher.py
    │   │   ├── KiprisPatentFetcher.py
    │   │   └── KiprisTrademarkFetcher.py
    │   ├── params
    │   │   ├── KiprisDesignPrams.py
    │   │   ├── KiprisPatentParams.py
    │   │   └── KiprisTrademarkParams.py
    │   ├── xml
    │   │   ├── KiprisXml.py
    │   │   ├── KiprisXmlData.py
    │   │   └── KiprisXmlDataGenerator.py
    └── upload
        ├── KiprisTB24DesignDataUploader.py
        ├── KiprisTB24PatentDataUploader.py
        └── KiprisTB24TrademarkDataUploader.py
└── util
    └── util.py

```

### 주요 클래스 및 기능 설명

#### 1. 데이터베이스 연동 (db/mysql.py)

* **`Mysql`**: MySQL 데이터베이스 연결 및 쿼리 실행을 위한 클래스.
    * `_connect_to_db()`: 데이터베이스 연결 설정.
    * `_get_cursor()`: 데이터베이스 커서 반환.
    * `get_cursor_fetchall(sql, *args)`: SQL 쿼리 실행 후 결과를 리스트 형태로 반환.
    * `insert_data_to_db(table_name, data_to_insert, use_executemany=True)`: 데이터베이스에 데이터 삽입.
    * `fetch_data_by_page(table_name, page, page_size, columns=None, filter_condition=None)`: 페이지 단위로 데이터 조회.
    * `upsert_data(table_name, data)`: 데이터 삽입 또는 업데이트 (upsert).
    * `fetch_data_from_db(table_name, columns=None, limit=None, filter_condition=None)`: 데이터베이스에서 데이터 조회.
    * `get_limit_app_no_and_applicant_id(limit)`: 제한된 수의 app_no와 applicant_id 조회.
    * `get_all_app_no_and_applicant_id(table='TB24_200')`: 모든 app_no와 applicant_id 조회.
    * `close_connection()`: 데이터베이스 연결 종료.


#### 2. KIPRIS 데이터 수집 (kipris/core/parsing)

* **`KiprisParams`**: KIPRIS API 요청 파라미터를 저장하는 클래스.
    * `app_no`:  출원 번호.
    * `applicant_id`: 출원인 ID.
    * `accessKey`: API 키.
    * `docsCount`: 페이지당 문서 수.
    * `docsStart`: 시작 문서 번호.
    * `applicant`: 출원인 이름 또는 번호.
    * `patent`, `utility`, `lastvalue`, `startNumber`, `etc`, `part`, `simi`, `abandonment`, `cancle`, `destroy`, `invalid`, `notice`, `open`, `registration`, `rejection`, `descSort`, `application`, `refused`, `expiration`, `withdrawal`, `publication`, `businessEmblem`, `certMark`, `collectiveMark`, `geoCertMark`, `geoOrgMark`, `internationalMark`, `serviceMark`, `trademark`, `trademarkServiceMark`, `character`, `compositionCharacter`, `figure`, `figureComposition`, `fragrance`, `sound`, `color`, `colorMixed`, `dimension`, `hologram`, `invisible`, `motion`, `visual`:  각 API에 따른 추가 파라미터.


* **`KiprisFetchData`**:  KIPRIS에서 가져온 데이터를 저장하는 클래스.
    * `applicant_number`: 출원 번호.
    * `applicant_id`: 출원인 ID.
    * `xml_str_list`: XML 문자열 리스트.

* **`KiprisFetcher`**:  KIPRIS API를 통해 데이터를 가져오는 클래스. 여러 개의 `KiprisParams`를 사용하여 비동기적으로 데이터를 가져올 수 있습니다.
    * `url`: API 엔드포인트 URL.
    * `params`: `KiprisParams` 객체 리스트.
    * `__task()`: 비동기적으로 데이터를 가져오는 내부 함수.
    * `get_infos()`: 여러 API 요청을 비동기적으로 실행하고 결과를 `KiprisFetchData` 객체 리스트로 반환.
    * `set_params()`: 파라미터 리스트 설정.

* **`KiprisApplicantInfoFetcher`**: 출원인 정보를 가져오는 클래스.
    * `url`: API 엔드포인트 URL.
    * `params`: `KiprisParams` 객체.
    * `result`: API 응답 결과 저장 리스트.
    * `max_pages`: 최대 페이지 수.
    * `success_count`: 성공한 요청 수.
    * `fail_count`: 실패한 요청 수.
    * `session`: aiohttp ClientSession 객체.
    * `open_session()`: ClientSession 열기.
    * `close_session()`: ClientSession 닫기.
    * `_fetch_content(page)`: 지정된 페이지의 데이터를 가져옴.
    * `__get_total_count(content)`: 전체 검색 결과 수 반환.
    * `_calculate_max_pages(total_count)`: 최대 페이지 수 계산.
    * `_handle_response(page)`: API 응답 처리 및 성공 여부 반환.
    * `_increment_page(page)`: 페이지 증가.
    * `fetch_initial()`: 첫 페이지 데이터 가져오기 및 전체 개수 계산.
    * `fetch_pages()`: 나머지 페이지 데이터 가져오기.
    * `get_info()`: 모든 데이터 가져오기 및 `KiprisFetchData` 객체 반환.

#### 3. 데이터 변환 (kipris/convert)

* **`KiprisMapping`**: KIPRIS API에서 사용하는 XML 태그와 데이터 필드 매핑 정보를 저장하는 클래스.
    * `ipr_seq`, `applicant_id`, `ipr_code`, `title`, `serial_no`, `applicant`, `appl_no`, `appl_date`, `pub_num`, `pub_date`, `legal_status_desc`, `image_path`, `inventor`, `agent`, `open_no`, `open_date`, `reg_no`, `reg_date`, `main_ipc`, `abstract`: 매핑 정보를 저장하는 속성.

* **`KiprisXmlToDictConverter`**: XML 데이터를 Python 딕셔너리로 변환하는 클래스.
    * `mapping`: `KiprisMapping` 객체.
    * `xml_filename`: XML 파일 이름.
    * `get_file_path(xml_filename)`: XML 파일 경로 생성.
    * `read_xml()`: XML 파일 읽어오기.
    * `parse(xpath_query)`: XML 데이터 파싱 및 딕셔너리 변환.

* **`KiprisDesignXmlToDictConverter`, `KiprisPatentXmlToDictConverter`, `KiprisTrademarkXmlToDictConverter`**: 각각 디자인, 특허, 상표 XML 데이터를 파싱하는 클래스. `KiprisXmlToDictConverter` 클래스를 상속받고, 각각에 맞는 XPath 쿼리를 사용합니다.

* **`DesignKiprisMapping`, `PatentKiprisMapping`, `TrademarkKiprisMapping`**: 각각 디자인, 특허, 상표 데이터에 대한 XML 태그와 필드 매핑 정보를 정의하는 클래스. `KiprisMapping` 클래스를 상속받습니다.


#### 4. KIPRIS XML 데이터 생성 및 저장 (kipris/parsing/xml)

* **`KiprisXml`**: XML 데이터를 생성하고 저장하는 기본 클래스.
    * `root`: XML 루트 요소.
    * `xml_to_string(xml)`: XML 요소를 문자열로 변환.
    * `save(file_name, file_path="")`: XML 파일 저장.
    * `clear()`: XML 데이터 초기화.

* **`KiprisXmlData`**: `KiprisFetchData` 객체를 XML 데이터로 변환하는 클래스. `KiprisXml` 클래스를 상속받습니다.
    * `data`: `KiprisFetchData` 객체.
    * `__get_base_xml()`: 기본 XML 템플릿 로드.
    * `fromstring(xml_str)`: XML 문자열을 파싱하여 `lxml.etree._Element` 객체로 변환.
    * `get_item_group_elem()`: 아이템 그룹 요소 반환.
    * `get_appli_id_elem()`: 출원인 ID 요소 반환.
    * `append_applicant_id()`: 출원인 ID 추가.
    * `append_items()`: 아이템 추가.
    * `get_merge_item_elem(xml_string)`: 여러 XML 문자열에서 아이템 병합.
    * `apply()`: 출원인 ID와 아이템을 XML에 추가.

* **`KiprisXmlDataGenerator`**: 여러 `KiprisFetchData` 객체를 하나의 XML 파일로 생성하는 클래스. `KiprisXml` 클래스를 상속받습니다.
    * `data_list`: `KiprisXmlData` 객체 리스트.
    * `append_data_list(fetch_data_list)`: `KiprisFetchData` 객체를 `data_list`에 추가.
    * `append_data_lists(fetch_data_list)`: 여러 `KiprisFetchData` 객체를 `data_list`에 추가.
    * `append_data_root()`: 모든 XML 데이터를 루트 요소에 추가.
    * `apply()`: XML 데이터 생성.
    * `clear()`: 데이터 초기화.
    * `save(file_name, file_path="")`: XML 파일 저장.


#### 5. 데이터 업로드 (kipris/upload)

* **`KiprisDataUploader`**:  KIPRIS 데이터를 데이터베이스에 업로드하는 기본 클래스.
    * `mysql`: `Mysql` 객체.
    * `table_name`: 업로드할 테이블 이름.
    * `upload(data)`: 데이터 업로드.

* **`KiprisTB24DesignDataUploader`, `KiprisTB24PatentDataUploader`, `KiprisTB24TrademarkDataUploader`**: 각각 디자인, 특허, 상표 데이터를 업로드하는 클래스. `KiprisDataUploader` 클래스를 상속받고, `table_name` 속성을 설정합니다.

#### 6. 유틸리티 함수 (util/util.py)

* **`get_timestamp()`**: 현재 시간을 타임스탬프 문자열로 반환.
* **`add_sys_path()`**: 현재 파일 디렉토리를 `sys.path`에 추가.
* **`get_run_time(callback, msg)`**: 콜백 함수 실행 시간 측정.
* **`clean_whitespace(text)`**: 문자열 공백 제거.
* **`split(text, seperator='|')`**: 문자열 분할.


