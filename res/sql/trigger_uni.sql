-- Active: 1731326975902@@kt2.elementsoft.biz@13306@kipris
-- 대학 트리거 


CREATE TRIGGER university_patent_insert_trigger
AFTER INSERT 
ON TB24_university_patent FOR EACH ROW
BEGIN
	INSERT INTO daily_update_university(ipr_seq, service_type, applicant, legal_status_desc)
VALUES (NEW.ipr_seq,"patent", NEW.applicant, NEW.legal_status_desc);
END



CREATE TRIGGER university_patent_update_trigger
AFTER UPDATE
ON TB24_university_patent FOR EACH ROW
BEGIN
	INSERT INTO daily_update_university(ipr_seq, service_type, applicant, legal_status_desc)
VALUES (NEW.ipr_seq,"patent", NEW.applicant, NEW.legal_status_desc);
END



CREATE TRIGGER university_design_insert_trigger
AFTER INSERT 
ON TB24_university_design FOR EACH ROW
BEGIN
	INSERT INTO daily_update_university(ipr_seq, service_type, applicant, legal_status_desc)
VALUES (NEW.ipr_seq,"design", NEW.applicant, NEW.legal_status_desc);
END



CREATE TRIGGER university_design_update_trigger
AFTER UPDATE
ON TB24_university_design FOR EACH ROW
BEGIN
	INSERT INTO daily_update_university(ipr_seq, service_type, applicant, legal_status_desc)
VALUES (NEW.ipr_seq,"design", NEW.applicant, NEW.legal_status_desc);
END



CREATE TRIGGER university_trademark_insert_trigger
AFTER INSERT 
ON TB24_university_trademark FOR EACH ROW
BEGIN
	INSERT INTO daily_update_university(ipr_seq, service_type, applicant, legal_status_desc)
VALUES (NEW.ipr_seq,"trademark", NEW.applicant, NEW.legal_status_desc);
END


CREATE TRIGGER university_trademark_update_trigger
AFTER UPDATE
ON TB24_university_trademark FOR EACH ROW
BEGIN
	INSERT INTO daily_update_university(ipr_seq, service_type, applicant, legal_status_desc)
VALUES (NEW.ipr_seq,"trademark", NEW.applicant, NEW.legal_status_desc);
END
