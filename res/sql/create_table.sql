-- Active: 1732169686429@@kt2.elementsoft.biz@13306@kipris
-- 기업정보

CREATE TABLE TB24_100 (
    company_seq INT AUTO_INCREMENT PRIMARY KEY,
    biz_no VARCHAR(12) NULL, 
    corp_no VARCHAR(15) NULL, 
    biz_type VARCHAR(5)  NULL,
    company_name VARCHAR(50) NOT NULL
);

-- 대학정보
CREATE TABLE TB24_110 (
    uni_seq INT AUTO_INCREMENT PRIMARY KEY,
    biz_no VARCHAR(12) NULL, 
    corp_no VARCHAR(15) NULL, 
    applicant VARCHAR(50) NOT NULL
);

-- 기업 특허고객번호
CREATE TABLE TB24_200 (
    applicant_id INT AUTO_INCREMENT PRIMARY KEY,
    applicant_no VARCHAR(20) UNIQUE,
    app_seq INT NOT NULL,
    write_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (app_seq) REFERENCES TB24_100(company_seq) ON DELETE CASCADE,
    app_type ENUM('company') NOT NULL
);

-- 대학 특허고객번호 
CREATE TABLE TB24_210 (
    applicant_id INT AUTO_INCREMENT PRIMARY KEY,
    applicant_no VARCHAR(20) UNIQUE,
    app_seq INT NOT NULL,
    write_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (app_seq) REFERENCES TB24_110(uni_seq) ON DELETE CASCADE,
    app_type ENUM('university') NOT NULL
);

-- 기업 특실 테이블
CREATE TABLE TB24_company_patent (
    ipr_seq INT AUTO_INCREMENT PRIMARY KEY,
    applicant_id INT NULL, -- TB24_200의 applicant_id 참조
    ipr_code VARCHAR(2),
    title VARCHAR(255) NOT NULL,
    serial_no VARCHAR(50),
    applicant VARCHAR(300),
    main_ipc VARCHAR(15),
    appl_no VARCHAR(50),
    appl_date DATE,
    open_no VARCHAR(50),
    open_date DATE,
    reg_no VARCHAR(50),
    reg_date DATE,
    pub_num VARCHAR(50),
    pub_date DATE,
    legal_status_desc VARCHAR(20),
    abstract TEXT,
    image_path TEXT,
    write_time DATETIME DEFAULT CURRENT_TIMESTAMP, -- 리얼타임으로 필드가 생성된 시간
    modify_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 수정 시간 자동 업데이트
    survey_year VARCHAR(5), -- 최초 수집시 조사 연도
    survey_month VARCHAR(5), -- 최초 수집시 조사 월
    FOREIGN KEY (applicant_id) REFERENCES TB24_200(applicant_id)
);

-- 기업 디자인 테이블
CREATE TABLE TB24_company_design (
    ipr_seq INT AUTO_INCREMENT PRIMARY KEY,
    applicant_id INT NULL, -- TB24_200의 applicant_id 참조
    ipr_code VARCHAR(2),
    title VARCHAR(255) NOT NULL,
    serial_no VARCHAR(50),
    applicant VARCHAR(300),
    inventor VARCHAR(100),
    agent VARCHAR(100),
    appl_no VARCHAR(50),
    appl_date DATE,
    open_no VARCHAR(50),
    open_date DATE,
    reg_no VARCHAR(50),
    reg_date DATE,
    pub_num VARCHAR(50),
    pub_date DATE,
    legal_status_desc VARCHAR(20),
    image_path TEXT,
    write_time DATETIME DEFAULT CURRENT_TIMESTAMP, -- 리얼타임으로 필드가 생성된 시간
    modify_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 수정 시간 자동 업데이트
    survey_year VARCHAR(5), -- 최초 수집시 조사 연도
    survey_month VARCHAR(5), -- 최초 수집시 조사 월
    FOREIGN KEY (applicant_id) REFERENCES TB24_200(applicant_id)
);

-- 기업 상표 테이블
CREATE TABLE TB24_company_trademark (
    ipr_seq INT AUTO_INCREMENT PRIMARY KEY,
    applicant_id INT NULL, -- TB24_200의 applicant_id 참조
    ipr_code VARCHAR(2),
    title VARCHAR(255) NOT NULL,
    serial_no VARCHAR(50),
    applicant VARCHAR(300) ,
    agent VARCHAR(100),
    appl_no VARCHAR(50),
    appl_date DATE,
    pub_num VARCHAR(50),
    pub_date DATE,
    legal_status_desc VARCHAR(20),
    image_path VARCHAR(255),
    write_time DATETIME DEFAULT CURRENT_TIMESTAMP, -- 리얼타임으로 필드가 생성된 시간
    modify_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 수정 시간 자동 업데이트
    survey_year VARCHAR(5), -- 최초 수집시 조사 연도
    survey_month VARCHAR(5), -- 최초 수집시 조사 월
    FOREIGN KEY (applicant_id) REFERENCES TB24_200(applicant_id)
);

-- 대학 특실 테이블
CREATE TABLE TB24_university_patent (
    ipr_seq INT AUTO_INCREMENT PRIMARY KEY,
    applicant_id INT NULL, -- TB24_210의 applicant_id 참조
    ipr_code VARCHAR(2),
    title VARCHAR(255) NOT NULL,
    serial_no VARCHAR(50),
    applicant VARCHAR(300),
    main_ipc VARCHAR(15),
    appl_no VARCHAR(50),
    appl_date DATE,
    open_no VARCHAR(50),
    open_date DATE,
    reg_no VARCHAR(50),
    reg_date DATE,
    pub_num VARCHAR(50),
    pub_date DATE,
    legal_status_desc VARCHAR(20),
    abstract TEXT,
    image_path TEXT,
    write_time DATETIME DEFAULT CURRENT_TIMESTAMP, -- 리얼타임으로 필드가 생성된 시간
    modify_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 수정 시간 자동 업데이트
    survey_year VARCHAR(5), -- 최초 수집시 조사 연도
    survey_month VARCHAR(5), -- 최초 수집시 조사 월
    FOREIGN KEY (applicant_id) REFERENCES TB24_210(applicant_id)
);

-- 대학 디자인 테이블
CREATE TABLE TB24_university_design (
    ipr_seq INT AUTO_INCREMENT PRIMARY KEY,
    applicant_id INT NULL, -- TB24_210의 applicant_id 참조
    ipr_code VARCHAR(2),
    title VARCHAR(255) NOT NULL,
    serial_no VARCHAR(50),
    applicant VARCHAR(300),
    inventor VARCHAR(100),
    agent VARCHAR(100),
    appl_no VARCHAR(50),
    appl_date DATE,
    open_no VARCHAR(50),
    open_date DATE,
    reg_no VARCHAR(50),
    reg_date DATE,
    pub_num VARCHAR(50),
    pub_date DATE,
    legal_status_desc VARCHAR(20),
    image_path TEXT,
    write_time DATETIME DEFAULT CURRENT_TIMESTAMP, -- 리얼타임으로 필드가 생성된 시간
    modify_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 수정 시간 자동 업데이트
    survey_year VARCHAR(5), -- 최초 수집시 조사 연도
    survey_month VARCHAR(5), -- 최초 수집시 조사 월
    FOREIGN KEY (applicant_id) REFERENCES TB24_210(applicant_id)
);

-- 대학 상표 테이블
CREATE TABLE TB24_university_trademark (
    ipr_seq INT AUTO_INCREMENT PRIMARY KEY,
    applicant_id INT NULL, -- TB24_200의 applicant_id 참조
    ipr_code VARCHAR(2),
    title VARCHAR(255) NOT NULL,
    serial_no VARCHAR(50),
    applicant VARCHAR(300),
    agent VARCHAR(100),
    appl_no VARCHAR(50),
    appl_date DATE,
    pub_num VARCHAR(50),
    pub_date DATE,
    legal_status_desc VARCHAR(20),
    image_path VARCHAR(255),
    write_time DATETIME DEFAULT CURRENT_TIMESTAMP, -- 리얼타임으로 필드가 생성된 시간
    modify_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 수정 시간 자동 업데이트
    survey_year VARCHAR(5), -- 최초 수집시 조사 연도
    survey_month VARCHAR(5), -- 최초 수집시 조사 월
    FOREIGN KEY (applicant_id) REFERENCES TB24_210(applicant_id)
);

-- 기업 IPC_CPC 테이블
CREATE TABLE TB24_310_company (
    ipc_seq INT AUTO_INCREMENT PRIMARY KEY,
    ipr_seq INT NOT NULL, -- TB24_company_patent 또는 TB24_university_patent의 ipr_seq 참조
    ipc_cpc VARCHAR(10),  -- IPC_CPC 구분
    ipc_cpc_code VARCHAR(20),  -- IPC_CPC 코드(ipcNumber)
    FOREIGN KEY (ipr_seq) REFERENCES TB24_company_patent(ipr_seq) ON DELETE CASCADE,
    CHECK (ipc_cpc IN ('IPC', 'CPC'))
);

ALTER TABLE TB24_310_company
ADD UNIQUE (ipr_seq, ipc_cpc_code);


-- 대학 IPC_CPC 테이블
CREATE TABLE TB24_310_university (
    ipc_seq INT AUTO_INCREMENT PRIMARY KEY,
    ipr_seq INT NOT NULL, -- TB24_company_patent 또는 TB24_university_patent의 ipr_seq 참조
    ipc_cpc VARCHAR(10),  -- IPC_CPC 구분
    ipc_cpc_code VARCHAR(20),  -- IPC_CPC 코드(ipcNumber)
    FOREIGN KEY (ipr_seq) REFERENCES TB24_university_patent(ipr_seq) ON DELETE CASCADE,
    CHECK (ipc_cpc IN ('IPC', 'CPC'))
);
ALTER TABLE TB24_310_university
ADD UNIQUE (ipr_seq, ipc_cpc_code);


-- 기업 우선권 테이블
CREATE TABLE TB24_320_company (
    priority_seq INT AUTO_INCREMENT PRIMARY KEY,
    ipr_seq INT NOT NULL,
    ipr_type ENUM('design', 'trademark') NOT NULL,
    priority_no VARCHAR(50) UNIQUE,
    priority_date DATE,
    CHECK (ipr_type IN ('design', 'trademark'))
);


ALTER TABLE TB24_320_company
ADD UNIQUE (ipr_seq, ipr_type, priority_no);

-- 대학 우선권 테이블
CREATE TABLE TB24_320_university (
    priority_seq INT AUTO_INCREMENT PRIMARY KEY,
    ipr_seq INT NOT NULL,              -- TB24_design 또는 TB24_trademark의 ipr_seq 참조
    ipr_type ENUM('design', 'trademark') NOT NULL, -- 참조 타입 구분
    priority_no VARCHAR(50) UNIQUE,    -- 우선권주장번호
    priority_date DATE,                -- 우선권주장일자
	CHECK (ipr_type IN ('design', 'trademark'))
);

ALTER TABLE TB24_320_university
ADD UNIQUE (ipr_seq, ipr_type, priority_no);

-- 기업 특실 테이블 인덱싱 추가(appl_no, applicant_id)
ALTER TABLE TB24_company_patent
ADD UNIQUE INDEX index_appl_no_applicant_id (appl_no, applicant_id,serial_no);

-- 기업 디자인 테이블 인덱싱 추가(appl_no, applicant_id)
ALTER TABLE TB24_company_design 
ADD UNIQUE INDEX index_appl_no_applicant_id (appl_no, applicant_id,serial_no);

-- 기업 상표 테이블 인덱싱 추가(appl_no, applicant_id)
ALTER TABLE TB24_company_trademark 
ADD UNIQUE INDEX index_appl_no_applicant_id (appl_no, applicant_id,serial_no);

-- 대학 특실 테이블 인덱싱 추가(appl_no, applicant_id)
ALTER TABLE TB24_university_patent
ADD UNIQUE INDEX index_appl_no_applicant_id (appl_no, applicant_id,serial_no);

-- 대학 디자인 테이블 인덱싱 추가(appl_no, applicant_id)
ALTER TABLE TB24_university_design
ADD UNIQUE INDEX index_appl_no_applicant_id (appl_no, applicant_id,serial_no);

-- 대학 상표 테이블 인덱싱 추가(appl_no, applicant_id)
ALTER TABLE TB24_university_trademark 
ADD UNIQUE INDEX index_appl_no_applicant_id (appl_no, applicant_id,serial_no);

