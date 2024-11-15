-- Active: 1731490907969@@localhost@3306@kipris
CREATE TABLE daily_update_company (
		daily_id INT AUTO_INCREMENT PRIMARY KEY,
		ipr_seq INT,
    service_type ENUM('design', 'trademark', 'patent') NOT NULL,
    applicant VARCHAR(300),
    legal_status_desc VARCHAR(20),
    update_date DATE  -- 날짜를 저장할 컬럼
);

CREATE TABLE daily_update_university (
		daily_id INT AUTO_INCREMENT PRIMARY KEY,
		ipr_seq INT,
    service_type ENUM('design', 'trademark', 'patent') NOT NULL,
    applicant VARCHAR(300),
    legal_status_desc VARCHAR(20),
    update_date DATE  -- 날짜를 저장할 컬럼
);

INSERT INTO kipris.TB24_310_company (ipc_cpc, ipc_cpc_code, ipr_seq)
SELECT
'IPC', 'H05K 7/06', ipr_seq
FROM
TB24_company_patent
WHERE
appl_no = 2020040031672 AND applicant_id = 4719 AND serial_no = 1;