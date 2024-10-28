create database neojune;
use neojune;

-- 기업정보
CREATE TABLE TB24_100 (
    company_seq INT AUTO_INCREMENT PRIMARY KEY,
    biz_no VARCHAR(12) NULL, 
    corp_no VARCHAR(15) NULL, 
    biz_type VARCHAR(5)  NULL,
    company_name VARCHAR(50)  NOT NULL
);

-- 대학 특허 고객번호
CREATE TABLE TB24_210(
    university_seq INT AUTO_INCREMENT PRIMARY KEY, 
    applicant_no BIGINT NULL,
    applicant  VARCHAR(500) NOT NULL,
    biz_no VARCHAR(12) NULL, 
    corp_no VARCHAR(15) NULL, 
    ref_desc VARCHAR(20) NULL, 
    write_time DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 기업 정보와 연동된 특허 고객번호 
CREATE TABLE TB24_200(
    applicant_id INT AUTO_INCREMENT PRIMARY KEY, 
    app_no VARCHAR(20), 
    compay_name VARCHAR(50), 
    corp_no VARCHAR(15),
    biz_no VARCHAR(12),
    company_seq INT,
    FOREIGN KEY (company_seq) REFERENCES TB24_100(company_seq)
);
ALTER TABLE TB24_200
ADD UNIQUE (app_no),
ADD write_time DATETIME DEFAULT CURRENT_TIMESTAMP,
ADD modify_time DATETIME ON UPDATE CURRENT_TIMESTAMP;

CREATE INDEX idx_app_no ON TB24_200(app_no);
CREATE INDEX idx_biz_no ON TB24_200(biz_no);
create database neojune;
use neojune;

-- 기업정보
CREATE TABLE TB24_100 (
    company_seq INT AUTO_INCREMENT PRIMARY KEY,
    biz_no VARCHAR(12) NULL, 
    corp_no VARCHAR(15) NULL, 
    biz_type VARCHAR(5)  NULL,
    company_name VARCHAR(50)  NOT NULL
);

-- 대학 특허 고객번호
CREATE TABLE TB24_210(
    university_seq INT AUTO_INCREMENT PRIMARY KEY, 
    applicant_no BIGINT NULL,
    applicant  VARCHAR(500) NOT NULL,
    biz_no VARCHAR(12) NULL, 
    corp_no VARCHAR(15) NULL, 
    ref_desc VARCHAR(20) NULL, 
    write_time DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 기업 정보와 연동된 특허 고객번호 
CREATE TABLE TB24_200(
    applicant_id INT AUTO_INCREMENT PRIMARY KEY, 
    app_no VARCHAR(20), 
    compay_name VARCHAR(50), 
    corp_no VARCHAR(15),
    biz_no VARCHAR(12),
    company_seq INT,
    FOREIGN KEY (company_seq) REFERENCES TB24_100(company_seq)
);
ALTER TABLE TB24_200
ADD UNIQUE (app_no),
ADD write_time DATETIME DEFAULT CURRENT_TIMESTAMP,
ADD modify_time DATETIME ON UPDATE CURRENT_TIMESTAMP;

CREATE INDEX idx_app_no ON TB24_200(app_no);

CREATE TABLE IF NOT EXISTS patent (
    ipr_seq INT AUTO_INCREMENT PRIMARY KEY,
    applicant_no VARCHAR(20) NOT NULL, -- TB24_200의 app_no 참조
    ipr_code VARCHAR(5),
    title VARCHAR(255),
    serial_no VARCHAR(50) UNIQUE,
    applicant VARCHAR(100),
    main_ipc VARCHAR(50),
    appl_no VARCHAR(50) UNIQUE,
    appl_date DATE,
    open_no VARCHAR(50),
    open_date DATE,
    reg_no VARCHAR(50),
    reg_date DATE,
    notification_num VARCHAR(50),
    notification_date DATE,
    legal_status_desc VARCHAR(20),
    abstract TEXT,
    image_path VARCHAR(255),
    write_time DATETIME DEFAULT CURRENT_TIMESTAMP, -- 리얼타임으로 필드가 생성된 시간
	modify_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 수정 시간 자동 업데이트
    survey_year VARCHAR(5), -- 최초 수집시 조사 연도
    survey_month VARCHAR(5), -- 최초 수집시 조사 월
    FOREIGN KEY (applicant_no) REFERENCES TB24_200(app_no)
);

CREATE TABLE IF NOT EXISTS design (
    ipr_seq INT AUTO_INCREMENT PRIMARY KEY,
    applicant_no VARCHAR(20) NOT NULL, -- TB24_200의 app_no 참조
    ipr_code VARCHAR(5),
    title VARCHAR(255),
    serial_no VARCHAR(50) UNIQUE,
    applicant VARCHAR(100),
    inventor VARCHAR(100),
    agent VARCHAR(100),
    appl_no VARCHAR(50) UNIQUE,
    appl_date DATE,
    open_no VARCHAR(50),
    open_date DATE,
    reg_no VARCHAR(50),
    reg_date DATE,
    notification_num VARCHAR(50),
    notification_date DATE,
    legal_status_desc VARCHAR(20),
    image_path VARCHAR(255),
    write_time DATETIME DEFAULT CURRENT_TIMESTAMP, -- 리얼타임으로 필드가 생성된 시간
		modify_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 수정 시간 자동 업데이트
    survey_year VARCHAR(5), -- 최초 수집시 조사 연도
    survey_month VARCHAR(5), -- 최초 수집시 조사 월
    FOREIGN KEY (applicant_no) REFERENCES TB24_200(app_no)
);

CREATE TABLE IF NOT EXISTS trademark (
    ipr_seq INT AUTO_INCREMENT PRIMARY KEY,
    applicant_no VARCHAR(20) NOT NULL, -- TB24_200의 app_no 참조
    ipr_code VARCHAR(5) NOT NULL,
    title VARCHAR(255) NOT NULL,
    serial_no VARCHAR(50),
    applicant VARCHAR(100),
    agent VARCHAR(100),
    ipcNumber VARCHAR(50),
    appl_no VARCHAR(50),
    appl_date DATE,
    notification_num VARCHAR(50),
    notification_date DATE,
    legal_status_desc VARCHAR(20),
    image_path VARCHAR(255),
    write_time DATETIME DEFAULT CURRENT_TIMESTAMP, -- 리얼타임으로 필드가 생성된 시간
		modify_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- 수정 시간 자동 업데이트
    survey_year VARCHAR(5), -- 최초 수집시 조사 연도
    survey_month VARCHAR(5), -- 최초 수집시 조사 월
    FOREIGN KEY (applicant_no) REFERENCES TB24_200(app_no)
);

CREATE TABLE tb24_320 (
    priority_seq VARCHAR(20) PRIMARY KEY,
    applicant_no VARCHAR(20) NOT NULL, -- TB24_200의 app_no 참조
    ipr_seq INT,
    priority_nation VARCHAR(200), -- 우선권주장국가
    priority_no VARCHAR(50) UNIQUE, -- 우선권주장번호
    priority_date DATE, -- 우선권주장일자
    FOREIGN KEY (applicant_no) REFERENCES TB24_200(app_no),
    FOREIGN KEY (ipr_seq) REFERENCES patent(ipr_seq)
);

CREATE TABLE tb24_320 (
    priority_seq VARCHAR(20) PRIMARY KEY,
    applicant_no VARCHAR(20) NOT NULL, -- TB24_200의 app_no 참조
    ipr_seq INT,
    ipc_cpc VARCHAR(10), -- IPC_CPC 구분
    ipc_cpc_code VARCHAR(20), -- IPC_CPC 코드
    FOREIGN KEY (applicant_no) REFERENCES TB24_200(app_no),
    FOREIGN KEY (ipr_seq) REFERENCES patent(ipr_seq)
);

show tables;

select * from tb24_320