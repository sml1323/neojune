-- Active: 1731326975902@@kt2.elementsoft.biz@13306@kipris
-- 기업 트리거

CREATE TRIGGER company_patent_insert_trigger
AFTER INSERT 
ON TB24_company_patent FOR EACH ROW
BEGIN
	INSERT INTO daily_update_company(ipr_seq, service_type, applicant, legal_status_desc)
VALUES (NEW.ipr_seq,"patent", NEW.applicant, NEW.legal_status_desc);
END

CREATE TRIGGER company_patent_update_trigger
AFTER UPDATE
ON TB24_company_patent FOR EACH ROW
BEGIN
	INSERT INTO daily_update_company(ipr_seq, service_type, applicant, legal_status_desc)
VALUES (NEW.ipr_seq,"patent", NEW.applicant, NEW.legal_status_desc);
END

CREATE TRIGGER company_design_insert_trigger
AFTER INSERT 
ON TB24_company_design FOR EACH ROW
BEGIN
	INSERT INTO daily_update_company(ipr_seq, service_type, applicant, legal_status_desc)
VALUES (NEW.ipr_seq,"design", NEW.applicant, NEW.legal_status_desc);
END 

CREATE TRIGGER company_design_update_trigger
AFTER UPDATE
ON TB24_company_design FOR EACH ROW
BEGIN
	INSERT INTO daily_update_company(ipr_seq, service_type, applicant, legal_status_desc)
VALUES (NEW.ipr_seq,"design", NEW.applicant, NEW.legal_status_desc);
END


CREATE TRIGGER company_trademark_insert_trigger
AFTER INSERT 
ON TB24_company_trademark FOR EACH ROW
BEGIN
	INSERT INTO daily_update_company(ipr_seq, service_type, applicant, legal_status_desc)
VALUES (NEW.ipr_seq,"trademark", NEW.applicant, NEW.legal_status_desc);
END



CREATE TRIGGER company_trademark_update_trigger
AFTER UPDATE
ON TB24_company_trademark FOR EACH ROW
BEGIN
	INSERT INTO daily_update_company(ipr_seq, service_type, applicant, legal_status_desc)
VALUES (NEW.ipr_seq,"trademark", NEW.applicant, NEW.legal_status_desc);
END






