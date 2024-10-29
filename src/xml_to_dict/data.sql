CREATE TABLE IF NOT EXISTS TB24_patent (
  ipr_seq INT AUTO_INCREMENT PRIMARY KEY,
  applicant_no VARCHAR(20) NOT NULL, -- TB24_200의 app_no 참조
  ipr_code VARCHAR(2),
  title VARCHAR(255),
  serial_no VARCHAR(50) UNIQUE,
  applicant VARCHAR(100),
  main_ipc VARCHAR(15),
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
  survey_month VARCHAR(5)
);


CREATE TABLE IF NOT EXISTS TB24_design (
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


CREATE TABLE IF NOT EXISTS TB24_trademark (
    ipr_seq INT AUTO_INCREMENT PRIMARY KEY,
    applicant_no VARCHAR(20) NOT NULL, -- TB24_200의 app_no 참조
    ipr_code VARCHAR(2),
    title VARCHAR(255) NOT NULL,
    serial_no VARCHAR(50),
    applicant VARCHAR(100),
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
    FOREIGN KEY (applicant_no) REFERENCES TB24_200(applicant_no)
);