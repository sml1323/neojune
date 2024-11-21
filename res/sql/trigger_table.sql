-- Active: 1732169686429@@kt2.elementsoft.biz@13306@kipris
CREATE TABLE daily_update_company (
		daily_id INT AUTO_INCREMENT PRIMARY KEY,
		ipr_seq INT,
    service_type ENUM('design', 'trademark', 'patent') NOT NULL,
    applicant VARCHAR(300),
    legal_status_desc VARCHAR(20),
    update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 날짜를 저장할 컬럼
);
ALTER TABLE daily_update_company
MODIFY COLUMN update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP;


CREATE TABLE daily_update_university (
		daily_id INT AUTO_INCREMENT PRIMARY KEY,
		ipr_seq INT,
    service_type ENUM('design', 'trademark', 'patent') NOT NULL,
    applicant VARCHAR(300),
    legal_status_desc VARCHAR(20),
    update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 날짜를 저장할 컬럼
);
ALTER TABLE daily_update_university
MODIFY COLUMN update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP;
