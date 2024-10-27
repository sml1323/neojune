## git 정보

- 주소: https://github.com/namugach/neojune/commits/reactory-api-models/
- 브랜치 이름: reactory-api-models
- 커밋 해시: 174c20e6e1684f75c569809de5870701c8f8bf84

---


## 모듈 구조

```
.
├── Kipris.py
└── module
    ├── KiprisBackFileDataGenerator.py
    ├── backfile_prop
    │   ├── DesingBackFileDataKeyProp.py
    │   ├── PatentBackFileDataKeyProp.py
    │   └── TrademarkBackFileDataKeyProp.py
    ├── core
    │   ├── KiprisBackFileDataKeyProp.py
    │   ├── KiprisObject.py
    │   ├── KiprisParams.py
    │   └── ServiceNames.py
    ├── params
    │   ├── DesingPrams.py
    │   ├── PatentParams.py
    │   └── TrademarkParams.py
    └── util.py
```

## 주요 클래스 및 기능

### 1. `Kipris` (Kipris.py)

* **역할:** KIPRIS API를 호출하고 데이터를 가져오는 핵심 클래스.
* **속성:**
    * `params` (KiprisParams): API 요청 파라미터 객체.
* **메소드:**
    * `get_response(applicant)`: 특정 출원인에 대한 API에 HTTP GET 요청을 보내고 `requests.Response` 객체를 반환.
    * `get_response_dict(applicant)`: API 응답을 XML에서 Python 딕셔너리로 파싱.
    * `get_body(applicant)`: 파싱된 응답에서 'body' 부분을 추출.
    * `get_item(applicant)`: 'body'에서 'items'의 'item' 리스트를 추출.
    * `prev_page()`: 현재 페이지 번호를 1 감소.
    * `next_page()`: 현재 페이지 번호를 1 증가.
    * `goto_page(page_number)`: 현재 페이지 번호를 지정된 페이지 번호로 설정.

### 2. `KiprisBackFileDataGenerator` (KiprisBackFileDataGenerator.py)

* **역할:** KIPRIS 백파일 데이터 생성.
* **속성:**
    * `params` (KiprisParams): KIPRIS 파라미터.
    * `key_prop` (dict): 백파일 데이터 키 속성 딕셔너리.
* **메소드:**
    * `create(item)`: 주어진 아이템 목록을 기반으로 백파일 데이터를 생성.

### 3. `DesignParams`, `PatentParams`, `TrademarkParams` (params 디렉토리)

* **역할:** 디자인, 특허, 상표 검색 API에 필요한 파라미터 설정.
* **상속:** `KiprisParams` 클래스를 상속.
* **메소드:** 각 API에 필요한 파라미터를 설정하는 메소드 (예: `set_applicantName()`, `set_applicationNumber()`, `set_keyword()`, `set_numOfRows()` 등)
    * `DesignParams`: 디자인 검색 파라미터 설정 (open, rejection, destroy, cancle, notice, registration, invalid, abandonment, simi, part, etc, sortSpec).
    * `PatentParams`:  특허 검색 파라미터 설정 (applicant).
    * `TrademarkParams`: 상표 검색 파라미터 설정 (freeSearch, application, registration, refused, expiration, withdrawal, publication, cancel, abandonment, serviceMark, trademark, trademarkServiceMark, businessEmblem, collectiveMark, internationalMark, character, figure, compositionCharacter, figureComposition, sound, fragrance, color, dimension, colorMixed, hologram, motion, visual, invisible, sortSpec).

### 4.  `DesignBackFileDataKeyProp`, `PatentBackFileDataKeyProp`, `TrademarkBackFileDataKeyProp` (backfile_prop 디렉토리)

* **역할:** 디자인, 특허, 상표 백파일 데이터 키 속성 정의.
* **상속:** `KiprisBackFileDataKeyProp` 클래스를 상속.
* **속성:**  각 백파일 데이터에 필요한 키 속성 (예: `index`, `title`, `legal_status_desc`, `drawing`)

### 5. `KiprisObject` (core/KiprisObject.py)

* **역할:** 기본적인 객체 기능 제공.
* **메소드:**
    * `get_dict()`: 객체를 딕셔너리 형태로 변환.

### 6. `KiprisParams` (core/KiprisParams.py)

* **역할:** KIPRIS API 파라미터 관리.
* **속성:**
    * `ServiceKey`: API 키.
    * `applicantName`: 특허번호
    * `applicant`: 특허번호
    * `freeSearch`: 특허번호
    * `pageNo`: 현재 페이지 번호.
    * `numOfRows`: 페이지당 표시할 최대 결과 수.
    * `serviceName`: 서비스 이름 (디자인, 특허, 상표).
* **메소드:**
    * `set_applicantName()`: 출원인 이름 설정.
    * `set_num_of_rows()`: 페이지당 표시할 최대 결과 수 설정.

### 7. `KiprisBackFileDataKeyProp` (core/KiprisBackFileDataKeyProp.py)

* **역할:** KIPRIS 백파일 데이터 키 속성 기본 정의.
* **속성:**  백파일 데이터에 필요한 키 속성 (예: `index`, `title`, `drawing`, `legal_status_desc`, `ipr_code`, `applicant`, `inventor`, `agent`, `appl_no`, `appl_date`, `open_no`, `open_date`, `reg_no`, `reg_date`, `pub_no`, `pub_date`, `ipc_number`).

### 8. `ServiceNames` (core/ServiceNames.py)

* **역할:**  KIPRIS API 서비스 이름을 Enum으로 정의.
* **값:** `DESIGN`, `PATENT`, `TRADEMARK`

### 9. `util` (util.py)

* **역할:** KIPRIS API 관련 유틸리티 함수 제공.
* **함수:**
    * `get_kipris_api_url()`: API 엔드포인트 URL 생성.

## 사용 예시

```python
from Kipris import Kipris
from module.KiprisBackFileDataGenerator import KiprisBackFileDataGenerator

from module.params.DesingPrams import DesingPrams
from module.backfile_prop.DesingBackFileDataKeyProp import DesingBackFileDataKeyProp

from module.params.TrademarkParams import TrademarkParams
from module.backfile_prop.TrademarkBackFileDataKeyProp import TrademarkBackFileDataKeyProp

from module.params.PatentParams import PatentParams
from module.backfile_prop.PatentBackFileDataKeyProp import PatentBackFileDataKeyProp

# 특허
patent_prams = PatentParams()
kipris = Kipris(patent_prams)
item = kipris.get_item("120160255942")

patent_backfile_data_key_prop = PatentBackFileDataKeyProp()
backfile_data_generator = KiprisBackFileDataGenerator(patent_prams, patent_backfile_data_key_prop)
print(backfile_data_generator.create(item))

# 상표
trademark_prams = TrademarkParams()
kipris = Kipris(trademark_prams)
item = kipris.get_item("120140558200")

trademark_backfile_data_key_prop = TrademarkBackFileDataKeyProp()
backfile_data_generator = KiprisBackFileDataGenerator(trademark_prams, trademark_backfile_data_key_prop)
print(backfile_data_generator.create(item))

# 디자인
desing_prams = DesingPrams()
kipris = Kipris(desing_prams)
item = kipris.get_item("420100417169")

desing_backfile_data_key_prop = DesingBackFileDataKeyProp()
backfile_data_generator = KiprisBackFileDataGenerator(desing_prams, desing_backfile_data_key_prop)
print(backfile_data_generator.create(item))

```
## 출력 결과

```python
# 특허
[
    {
        'index': '1',
        'title': '바이페린 억제제를 유효성분으로 포함하는 대사질환의 예방 또는 치료용 조성물',
        'drawing': 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e22d01c5c32ba711cf6c44017b7be89802c7adbeb8ee864227ad29af71a0a992e2d227cd08ca33b6403e083ad58cb2e6d18b2b1f44efbaff566c588263f66fe24c',
        'legal_status_desc': '등록',
        'ipr_code': None,
        'applicant': '120160255942',
        'inventor': None,
        'agent': None,
        'appl_no': '1020190112714',
        'appl_date': '20190911',
        'open_no': None,
        'open_date': None,
        'reg_no': '1021769370000',
        'reg_date': '20201104',
        'pub_no': None,
        'pub_date': '20201110',
        'ipc_number': 'A61K 48/00|A61K 31/36|A61K 39/395|A61K 45/06|A61P 3/00'
    }
]


# 상표
[
    {
        'index': '1',
        'title': 'June Soft',
        'drawing': 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e251697a9d72a9134459b0ed09a289f737644fe6d2d2c00485c7ba3f92040e0485115f13e34f1fe30a',
        'legal_status_desc': '거절',
        'ipr_code': None,
        'applicant': '120140558200',
        'inventor': None,
        'agent': None,
        'appl_no': '4020150019080',
        'appl_date': '20150316',
        'open_no': None,
        'open_date': None,
        'reg_no': None,
        'reg_date': None,
        'pub_no': None,
        'pub_date': None,
        'ipc_number': None
    },
]


# 디자인
[
    {
        'index': '1',
        'title': '마우스',
        'drawing': 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e29e0b68f68d514bb024d94985b7e63279193a503442dfdb64b6813453d29b34c4de5f9dae3dd00c4181e37563b6c28deac7709b1f7d16f45d',
        'legal_status_desc': '소멸',
        'ipr_code': None,
        'applicant': '420100417169',
        'inventor': None,
        'agent': None,
        'appl_no': '3020130051081',
        'appl_date': '20131008',
        'open_no': None,
        'open_date': None,
        'reg_no': None,
        'reg_date': None,
        'pub_no': None,
        'pub_date': '20140529',
        'ipc_number': None
    },
]
```


