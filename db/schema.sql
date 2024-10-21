
create database NEW_SCHEMA;
use NEW_SCHEMA;

-- TB_24_200_출원인
CREATE TABLE `NEW_SCHEMA`.`tb_24_200_applicant` (
    `applicant_no`    VARCHAR(20)  NOT NULL COMMENT '특허 고객번호', -- 특허 고객번호
    `applicant_name`  VARCHAR(500) NOT NULL COMMENT '출원인명', -- 출원인명
    `corp_no`         VARCHAR(20)  NOT NULL COMMENT '법인 등록번호', -- 법인 등록번호
    `biz_no`          VARCHAR(20)  NOT NULL COMMENT '사업자 등록번호', -- 사업자 등록번호
    `write_time`      DATETIME     NOT NULL COMMENT '등록 일시', -- 등록 일시
    `modify_time`     DATETIME     NULL     COMMENT '수정 일시', -- 수정 일시
    `ref_desc`        VARCHAR(500) NULL     COMMENT '비고' -- 비고
)
COMMENT 'TB_24_200_출원인';

-- TB_24_200_출원인 Primary Key 설정
ALTER TABLE `NEW_SCHEMA`.`tb_24_200_applicant`
    ADD CONSTRAINT `PK_tb_24_200_applicant` -- TB_24_200_출원인 Primary key
    PRIMARY KEY (`applicant_no`);


-- TB24_300_산업재산권 목록
CREATE TABLE `NEW_SCHEMA`.`tb24_300_industrial_property` (
    `ipr_seq`         INT          NOT NULL COMMENT 'IPR 일련번호', -- IPR 일련번호
    `applicant_no`    VARCHAR(20)  NOT NULL COMMENT '특허 고객번호', -- 특허 고객번호
    `biz_no`          VARCHAR(20)  NULL     COMMENT '사업자 등록번호', -- 사업자 등록번호
    `ipr_code`        CHAR(2)      NULL     COMMENT '권리 구분 코드 (특허:10 / 실용신안:20 / 디자인:30 / 상표:40)', -- 권리 구분 코드
    `applicant`       VARCHAR(500) NULL     COMMENT '출원인', -- 출원인
    `inventor`        VARCHAR(500) NULL     COMMENT '발명자', -- 발명자
    `agent`           VARCHAR(500) NULL     COMMENT '대리인', -- 대리인
    `main_ipc`        VARCHAR(20)  NULL     COMMENT '대표 IPC', -- 대표 IPC
    `appl_no`         VARCHAR(20)  NULL     COMMENT '출원 번호', -- 출원 번호
    `appl_date`       CHAR(8)      NULL     COMMENT '출원 일자', -- 출원 일자
    `open_no`         VARCHAR(20)  NULL     COMMENT '공개 번호', -- 공개 번호
    `open_date`       CHAR(8)      NULL     COMMENT '공개 일자', -- 공개 일자
    `reg_no`          VARCHAR(20)  NULL     COMMENT '등록 번호', -- 등록 번호
    `reg_date`        CHAR(8)      NULL     COMMENT '등록 일자', -- 등록 일자
    `int_appl_no`     VARCHAR(50)  NULL     COMMENT '국제 출원 번호', -- 국제 출원 번호
    `int_appl_date`   CHAR(8)      NULL     COMMENT '국제 출원 일자', -- 국제 출원 일자
    `int_open_no`     VARCHAR(50)  NULL     COMMENT '국제 공개 번호', -- 국제 공개 번호
    `int_open_date`   CHAR(8)      NULL     COMMENT '국제 공개 일자', -- 국제 공개 일자
    `legal_status_desc` VARCHAR(20) NULL    COMMENT '법적 상태', -- 법적 상태
    `exam_flag`       CHAR(1)      NULL     COMMENT '심사청구 여부', -- 심사청구 여부
    `exam_date`       CHAR(8)      NULL     COMMENT '심사청구 일자', -- 심사청구 일자
    `claim_cnt`       INT          NULL     COMMENT '심사 청구항수', -- 청구항의 개수
    `abstract`        CHAR(2000)   NULL     COMMENT '요약', -- 특허 요약
    `title`           VARCHAR(500) NULL     COMMENT '발명의 명칭', -- 명칭 (상표명, 디자인명)
    `write_time`      DATETIME     NOT NULL COMMENT '등록 일시', -- 등록 일시
    `modify_time`     DATETIME     NULL     COMMENT '수정 일시', -- 수정 일시
    `survey_year`     CHAR(4)      NULL     COMMENT '조사 연도', -- 최초 수집시 조사 연도
    `survey_month`    CHAR(2)      NULL     COMMENT '조사 월' -- 최초 수집시 조사 월
)
COMMENT 'TB24_300_산업재산권 목록';

-- TB24_300_산업재산권 목록 Primary Key 설정
ALTER TABLE `NEW_SCHEMA`.`tb24_300_industrial_property`
    ADD CONSTRAINT `PK_tb24_300_industrial_property` -- TB24_300 Primary key
    PRIMARY KEY (`ipr_seq`, `applicant_no`);

-- TB24_300 테이블에서 TB24_200 테이블의 applicant_no를 외래 키로 설정
ALTER TABLE `NEW_SCHEMA`.`tb24_300_industrial_property`
    ADD CONSTRAINT `FK_tb24_300_applicant_no` -- 외래 키 (applicant_no)
    FOREIGN KEY (`applicant_no`)
    REFERENCES `NEW_SCHEMA`.`tb24_200_applicant` (`applicant_no`);
-- TB24_320_우선권
CREATE TABLE `NEW_SCHEMA`.`tb24_320_priority` (
	`ipr_seq`         INT          NOT NULL COMMENT 'IPR 일련번호', -- IPR 일련번호
	`applicant_no`    VARCHAR(20)  NOT NULL COMMENT '특허 고객번호', -- 특허 고객번호
	`priority_seq`    INT          NOT NULL COMMENT '우선권 일련번호', -- 우선권 일련번호
	`priority_nation` VARCHAR(200) NULL     COMMENT '우선권 국가', -- 우선권 국가
	`priority_no`     VARCHAR(50)  NULL     COMMENT '우선권 번호', -- 우선권 번호
	`priority_date`   CHAR(8)      NULL     COMMENT '우선권 일자' -- 우선권 일자
)
COMMENT 'TB24_320_우선권';

-- TB24_320_우선권
ALTER TABLE `NEW_SCHEMA`.`tb24_320_priority`
	ADD CONSTRAINT `PK_tb24_320_priority` -- TB24_320_우선권 Primary key
	PRIMARY KEY (
	`ipr_seq`,      -- IPR 일련번호
	`applicant_no`, -- 특허 고객번호
	`priority_seq`  -- 우선권 일련번호
	);
	
-- TB24_320_우선권 외래 키 설정
ALTER TABLE `NEW_SCHEMA`.`tb24_320_priority`
    ADD CONSTRAINT `FK_tb24_320_priority_applicant_no` -- 외래 키 (applicant_no)
    FOREIGN KEY (`applicant_no`)
    REFERENCES `NEW_SCHEMA`.`tb24_300_industrial_property` (`applicant_no`),
    
    ADD CONSTRAINT `FK_tb24_320_priority_ipr_seq` -- 외래 키 (ipr_seq)
    FOREIGN KEY (`ipr_seq`)
    REFERENCES `NEW_SCHEMA`.`tb24_300_industrial_property` (`ipr_seq`);
-- TB24_310_IPC_CPC
CREATE TABLE `NEW_SCHEMA`.`tb24_310_ipc_cpc` (
	`ipr_seq`      INT         NOT NULL COMMENT 'IPR 일련번호', -- IPR 일련번호
	`applicant_no` VARCHAR(20) NOT NULL COMMENT '특허 고객번호', -- 특허 고객번호
	`ipc_seq`      INT         NOT NULL COMMENT 'IPC 일련번호', -- IPC 일련번호
	`ipc_cpc`      VARCHAR(10) NULL     COMMENT 'IPC_CPC 구분', -- IPC_CPC 구분
	`ipc_cpc_code` VARCHAR(20) NULL     COMMENT 'IPC_CPC 코드' -- IPC_CPC 코드
)
COMMENT 'TB24_310_IPC_CPC';

-- TB24_310_IPC_CPC
ALTER TABLE `NEW_SCHEMA`.`tb24_310_ipc_cpc`
	ADD CONSTRAINT `PK_tb24_310_ipc_cpc` -- TB24_310_IPC_CPC Primary key
	PRIMARY KEY (
	`ipr_seq`,      -- IPR 일련번호
	`applicant_no`, -- 특허 고객번호
	`ipc_seq`       -- IPC 일련번호
	);
	
-- TB24_310_IPC_CPC 외래 키 설정
ALTER TABLE `NEW_SCHEMA`.`tb24_310_ipc_cpc`
    ADD CONSTRAINT `FK_tb24_310_ipc_cpc_applicant_no` -- 외래 키 (applicant_no)
    FOREIGN KEY (`applicant_no`)
    REFERENCES `NEW_SCHEMA`.`tb24_300_industrial_property` (`applicant_no`),
    
    ADD CONSTRAINT `FK_tb24_310_ipc_cpc_ipr_seq` -- 외래 키 (ipr_seq)
    FOREIGN KEY (`ipr_seq`)
    REFERENCES `NEW_SCHEMA`.`tb24_300_industrial_property` (`ipr_seq`);
-- TB24_210 대학교 고객번호
CREATE TABLE `NEW_SCHEMA`.`tb24_210_university_applicant` (
    `applicant_no`    VARCHAR(20)  NOT NULL COMMENT '특허 고객번호', -- 특허 고객번호
    `applicant`       VARCHAR(500) NOT NULL COMMENT '출원인명', -- 출원인명
    `corp_no`         VARCHAR(20)  NULL     COMMENT '법인번호', -- 법인번호
    `biz_no`          VARCHAR(20)  NULL     COMMENT '사업자번호', -- 사업자번호
    `ref_desc`        VARCHAR(500) NULL     COMMENT '비고', -- 비고
    `write_time`      DATETIME     NOT NULL COMMENT '등록 일시' -- 등록 일시
)
COMMENT 'TB24_210 대학교 고객번호';

-- TB24_210 대학교 고객번호 Primary Key 설정
ALTER TABLE `NEW_SCHEMA`.`tb24_210_university_applicant`
    ADD CONSTRAINT `PK_tb24_210_university_applicant` -- Primary Key
    PRIMARY KEY (`applicant_no`);
-- TB24_400 대학교 산업재산권 목록
CREATE TABLE `NEW_SCHEMA`.`tb24_400_university_industrial_property` (
    `ipr_seq`         INT          NOT NULL COMMENT '일련번호', -- IPR 일련번호
    `applicant_no`    VARCHAR(20)  NOT NULL COMMENT '특허 고객번호', -- 특허 고객번호 (Foreign Key)
    `biz_no`          VARCHAR(20)  NULL     COMMENT '사업자 등록번호', -- 사업자 등록번호
    `biz_no2`         VARCHAR(20)  NULL     COMMENT '사업자 등록번호2', -- 사업자 등록번호2
    `ipr_code`        CHAR(2)      NULL     COMMENT '권리 구분 코드 (특허:10 / 실용신안:20 / 디자인:30 / 상표:40)', -- 권리 구분 코드
    `applicant`       VARCHAR(500) NULL     COMMENT '출원인', -- 대표 출원인 1명
    `inventor`        VARCHAR(500) NULL     COMMENT '발명자', -- 대표 발명자 1명
    `agent`           VARCHAR(500) NULL     COMMENT '대리인', -- 대표 대리인 1명
    `main_ipc`        VARCHAR(20)  NULL     COMMENT '대표 IPC', -- 대표 IPC 1건
    `appl_no`         VARCHAR(20)  NULL     COMMENT '출원 번호', -- 출원 번호
    `appl_date`       CHAR(8)      NULL     COMMENT '출원 일자', -- 출원 일자
    `open_no`         VARCHAR(20)  NULL     COMMENT '공개 번호', -- 공개 번호
    `open_date`       CHAR(8)      NULL     COMMENT '공개 일자', -- 공개 일자
    `reg_no`          VARCHAR(20)  NULL     COMMENT '등록 번호', -- 등록 번호
    `reg_date`        CHAR(8)      NULL     COMMENT '등록 일자', -- 등록 일자
    `int_appl_no`     VARCHAR(50)  NULL     COMMENT '국제 출원 번호', -- 국제 출원 번호
    `int_appl_date`   CHAR(8)      NULL     COMMENT '국제 출원 일자', -- 국제 출원 일자
    `int_open_no`     VARCHAR(50)  NULL     COMMENT '국제 공개 번호', -- 국제 공개 번호
    `int_open_date`   CHAR(8)      NULL     COMMENT '국제 공개 일자', -- 국제 공개 일자
    `legal_status_desc` VARCHAR(20) NULL    COMMENT '법적 상태', -- 법적 상태
    `exam_flag`       CHAR(1)      NULL     COMMENT '심사청구 여부', -- 심사청구 여부
    `exam_date`       CHAR(8)      NULL     COMMENT '심사청구 일자', -- 심사청구 일자
    `claim_cnt`       INT          NULL     COMMENT '청구항의 개수', -- 청구항의 개수
    `abstract`        CHAR(2000)   NULL     COMMENT '요약', -- 특허 요약
    `title`           VARCHAR(500) NULL     COMMENT '발명의 명칭 (상표명, 디자인명)', -- 명칭 (상표명, 디자인명)
    `write_time`      DATETIME     NOT NULL COMMENT '등록 일시', -- 등록 일시
    `modify_time`     DATETIME     NULL     COMMENT '수정 일시', -- 수정 일시
    `survey_year`     CHAR(4)      NULL     COMMENT '조사 연도', -- 최초 수집시 조사 연도
    `survey_month`    CHAR(2)      NULL     COMMENT '조사 월' -- 최초 수집시 조사 월
)
COMMENT 'TB24_400 대학교 산업재산권 목록';

-- Primary Key (복합 키: ipr_seq와 applicant_no) 설정
ALTER TABLE `NEW_SCHEMA`.`tb24_400_university_industrial_property`
    ADD CONSTRAINT `PK_tb24_400_university_industrial_property` -- Primary Key
    PRIMARY KEY (`ipr_seq`, `applicant_no`);

-- TB24_400에서 TB24_210의 특허 고객번호 참조 (Foreign Key)
ALTER TABLE `NEW_SCHEMA`.`tb24_400_university_industrial_property`
    ADD CONSTRAINT `FK_tb24_400_applicant_no` -- 외래 키 (applicant_no)
    FOREIGN KEY (`applicant_no`)
    REFERENCES `NEW_SCHEMA`.`tb24_210_university_applicant` (`applicant_no`);
-- TB24_410 IPC_CPC 테이블 생성
CREATE TABLE `NEW_SCHEMA`.`tb24_410_ipc_cpc` (
    `ipr_seq`         INT          NOT NULL COMMENT 'IPR 일련번호', -- IPR 일련번호 (Foreign Key)
    `applicant_no`    VARCHAR(20)  NOT NULL COMMENT '특허 고객번호', -- 특허 고객번호 (Foreign Key)
    `ipc_seq`         INT          NOT NULL COMMENT 'IPC 일련번호', -- IPC 일련번호
    `ipr_seq2`        INT          NOT NULL COMMENT '일련번호', -- 추가 일련번호
    `ipc_cpc`         VARCHAR(10)  NULL     COMMENT 'IPC_CPC 구분', -- IPC/CPC 구분
    `ipc_cpc_code`    VARCHAR(20)  NULL     COMMENT 'IPC_CPC 코드' -- IPC/CPC 코드
)
COMMENT 'TB24_410 IPC_CPC';

-- Primary Key 설정 (복합 키: ipr_seq, applicant_no, ipc_seq, ipr_seq2)
ALTER TABLE `NEW_SCHEMA`.`tb24_410_ipc_cpc`
    ADD CONSTRAINT `PK_tb24_410_ipc_cpc` -- Primary Key
    PRIMARY KEY (`ipr_seq`, `applicant_no`, `ipc_seq`, `ipr_seq2`);

-- TB24_410 테이블에서 TB24_400 테이블의 ipr_seq와 applicant_no를 참조하는 외래 키 설정
ALTER TABLE `NEW_SCHEMA`.`tb24_410_ipc_cpc`
    ADD CONSTRAINT `FK_tb24_410_applicant_no` -- 외래 키 (applicant_no)
    FOREIGN KEY (`applicant_no`)
    REFERENCES `NEW_SCHEMA`.`tb24_400_university_industrial_property` (`applicant_no`),

    ADD CONSTRAINT `FK_tb24_410_ipr_seq` -- 외래 키 (ipr_seq)
    FOREIGN KEY (`ipr_seq`)
    REFERENCES `NEW_SCHEMA`.`tb24_400_university_industrial_property` (`ipr_seq`);
-- TB24_420 우선권 테이블 생성
CREATE TABLE `NEW_SCHEMA`.`tb24_420_priority` (
    `priority_seq`    INT          NOT NULL COMMENT '우선권 일련번호', -- 우선권 일련번호
    `ipr_seq`         INT          NOT NULL COMMENT 'IPR 일련번호', -- IPR 일련번호 (Foreign Key)
    `applicant_no`    VARCHAR(20)  NOT NULL COMMENT '특허 고객번호', -- 특허 고객번호 (Foreign Key)
    `priority_nation` VARCHAR(200) NULL     COMMENT '우선권 국가', -- 우선권 국가
    `priority_no`     VARCHAR(50)  NULL     COMMENT '우선권 번호', -- 우선권 번호
    `priority_date`   CHAR(8)      NULL     COMMENT '우선권 일자' -- 우선권 일자
)
COMMENT 'TB24_420 우선권';

-- Primary Key 설정 (복합 키: priority_seq, ipr_seq, applicant_no)
ALTER TABLE `NEW_SCHEMA`.`tb24_420_priority`
    ADD CONSTRAINT `PK_tb24_420_priority` -- Primary Key
    PRIMARY KEY (`priority_seq`, `ipr_seq`, `applicant_no`);

-- TB24_420 테이블에서 TB24_400 테이블의 ipr_seq와 applicant_no를 참조하는 외래 키 설정
ALTER TABLE `NEW_SCHEMA`.`tb24_420_priority`
    ADD CONSTRAINT `FK_tb24_420_applicant_no` -- 외래 키 (applicant_no)
    FOREIGN KEY (`applicant_no`)
    REFERENCES `NEW_SCHEMA`.`tb24_400_university_industrial_property` (`applicant_no`),

    ADD CONSTRAINT `FK_tb24_420_ipr_seq` -- 외래 키 (ipr_seq)
    FOREIGN KEY (`ipr_seq`)
    REFERENCES `NEW_SCHEMA`.`tb24_400_university_industrial_property` (`ipr_seq`);
