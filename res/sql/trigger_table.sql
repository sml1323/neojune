-- Active: 1731326975902@@kt2.elementsoft.biz@13306@kipris
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
