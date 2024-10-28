-- Active: 1729489267608@@127.0.0.1@3306@mydatabase
create database neojune;
use neojune;
drop database neojune;

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
show tables;
SELECT * FROM TB24_100;

ALTER TABLE TB24_200
ADD UNIQUE (app_no);

CREATE TABLE TB24_300(
    ipr_id INT AUTO_INCREMENT PRIMARY KEY,
    ipr_seq VARCHAR(20),
    applicant_no VARCHAR(20), 
    biz_no VARCHAR(12),
    ipr_code VARCHAR(5),
    title VARCHAR(255),
    applicant VARCHAR(100),
    inventor VARCHAR(100),
    agent VARCHAR(100),
    ipcNumber VARCHAR(50),
    appl_no VARCHAR(50),
    appl_date DATE,
    open_no VARCHAR(50),
    open_date DATE,
    reg_no VARCHAR(50),
    reg_date DATE,
    legal_status_desc VARCHAR(20),
    abstract TEXT,
    -- 데이터 출처 확인 필요
    int_appl_no VARCHAR(50),
    int_appl_date DATE,
    int_open_no VARCHAR(50),
    int_open_date DATE,
    exam_flag VARCHAR(50),
    exam_date DATE,
    claim_cnt VARCHAR(20),
    write_time DATETIME,
    modify_time DATETIME,
    survey_year DATETIME DEFAULT CURRENT_TIMESTAMP,
    survey_month DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (applicant_no) REFERENCES TB24_200(app_no)
);
