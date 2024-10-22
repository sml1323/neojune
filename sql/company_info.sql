use neojune;

CREATE TABLE company_info (
    company_seq INT AUTO_INCREMENT PRIMARY KEY,
    biz_no BIGINT NULL, 
    corp_no VARCHAR(13) NULL, 
    biz_type VARCHAR(5)  NULL,
    company_name VARCHAR(50)  NOT NULL
);

CREATE TABLE university_info(
    university_seq INT AUTO_INCREMENT PRIMARY KEY, 
    applicant_no BIGINT NULL,
    applicant  VARCHAR(50) NOT NULL,
    biz_no VARCHAR(10) NULL, 
    corp_no VARCHAR(13) NULL, 
    ref_desc VARCHAR(20) NULL, 
    write_time DATETIME DEFAULT CURRENT_TIMESTAMP
)