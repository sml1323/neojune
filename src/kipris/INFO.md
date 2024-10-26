## git 정보

- 주소: https://github.com/namugach/neojune/commits/reactory-api-models/
- 브랜치 이름: reactory-api-models
- 커밋 해시: 5e347150043cb1d1ccb8eb451585f4b89eaf7808a

---



## 모듈 구조

```
└── module
    ├── core
    │   ├── KiprisObject.py
    │   └── KiprisParams.py
    ├── DesingPrams.py
    ├── IPDataConverter.py
    ├── PatentParams.py
    ├── TrademarkParams.py
    └── util.py

```

---

## 주요 클래스 및 기능

### 1. `Kipris` (Kipris.py)

* 역할: KIPRIS API를 호출하고 데이터를 가져오는 핵심 클래스
* 속성:
    * `url` (str): API 엔드포인트 URL
    * `params` (KiprisParams): API 요청 파라미터 객체
* 메소드:
    * `get_response()`: API에 HTTP GET 요청을 보내고 `requests.Response` 객체를 반환합니다.
    * `get_response_dict()`: API 응답을 XML에서 Python 딕셔너리로 파싱합니다.
    * `get_body()`: 파싱된 응답에서 'body' 부분을 추출합니다.
    * `get_item()`: 'body'에서 'items'의 'item' 리스트를 추출합니다.
    * `get_data()`: API에서 받은 데이터를 `IPDataConverter` 객체 리스트로 변환합니다.
    * `prev_page()`: 현재 페이지 번호를 1 감소시킵니다.
    * `next_page()`: 현재 페이지 번호를 1 증가시킵니다.
    * `goto_page()`: 현재 페이지 번호를 지정된 페이지 번호로 설정합니다.

### 2. `IPDataConverter` (IPDataConverter.py)

* 역할: KIPRIS API에서 반환된 데이터를 표준화된 형식으로 변환합니다.
* 속성:
    * `index`, `title`, `applicant`, `inventor`, `agent`, `appl_no`, `appl_date`, `open_no`, `open_date`, `reg_no`, `reg_date`, `pub_no`, `pub_date`, `legal_status_desc`, `drawing`, `ipcNumber`: KIPRIS API 응답 데이터 필드에 대응하는 속성들 (자세한 내용은 코드 주석 참조)
* 메소드:
    * `get_all_keys()`: 객체의 모든 속성 이름을 리스트로 반환합니다.
    * `get_convert_data()`: 단일 아이템 딕셔너리를 `IPDataConverter` 클래스의 구조에 맞게 변환합니다.
    * `get_convert_datas()`: 단일 아이템 또는 아이템 리스트를 `IPDataConverter` 구조로 변환합니다.

### 3. `PatentParams`, `TrademarkParams`, `DesignParams`

* 역할:  각각 특허, 상표, 디자인 검색 API에 필요한 파라미터를 설정하는 클래스
* 상속: `KiprisParams` 클래스를 상속받습니다.
* 메소드:
    * 각 API에 필요한 파라미터를 설정하는 메소드 (예: `set_applicantName()`, `set_applicationNumber()`, `set_keyword()`, `set_numOfRows()` 등)

### 4. `KiprisObject` (core/KiprisObject.py)

* 역할:  기본적인 객체 기능을 제공하는 클래스
* 메소드:
    * `get_dict()`: 객체를 딕셔너리 형태로 변환합니다.

### 5. `KiprisParams` (core/KiprisParams.py)

* 역할:  KIPRIS API 파라미터를 관리하는 기본 클래스
* 속성:
    * `ServiceKey`: API 키
    * `applicantName`: 출원인 이름
    * `pageNo`: 현재 페이지 번호
    * `numOfRows`: 페이지당 표시할 최대 결과 수
* 메소드:
    * `set_applicantName()`: 출원인 이름을 설정합니다.
    * `set_num_of_rows()`: 페이지당 표시할 최대 결과 수를 설정합니다.

### 6. `util` (util.py)

* 역할:  KIPRIS API 관련 유틸리티 함수 제공
* 함수:
    * `get_kipris_api_url()`: API 엔드포인트 URL을 생성합니다.

## 사용 예시

```python
from Kipris import Kipris
from module.PatentParams import PatentParams

# 환경 변수에서 API 키 불러오기
service_key = os.getenv('SERVICE_KEY')

# 특허 검색 파라미터 설정
patent_params = PatentParams(service_key)
patent_params.set_applicantName("120140558200")

# Kipris 객체 생성 및 데이터 가져오기
kipris = Kipris(util.get_kipris_api_url("patUtiModInfoSearchSevice"), patent_params)
patent_data = kipris.get_data()

# 결과 출력
print(patent_data)
```

## 출력 결과
```json
[
  {
    'agent': {},
    'appl_date': '20161229',
    'appl_no': '1020160182094',
    'applicant': {},
    'drawing': 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e22d01c5c32ba711cfcafa1947147e7af93520e6fdba6ed2dbe05227459c2502cde8994a6e47b340397a1360d1c15a24b20ca79a36e9bc19d4f4b5cfdca93330ba',
    'index': '1',
    'inventor': {},
    'ipcNumber': 'G06Q 50/10|G06Q 30/04|G06Q 30/02',
    'legal_status_desc': '거절',
    'open_date': '20180709',
    'open_no': '1020180077594',
    'pub_date': None,
    'pub_no': None,
    'reg_date': None,
    'reg_no': None,
    'title': '특허공보 번역 서비스 제공 시스템 및 그 방법'
  }
]
```

