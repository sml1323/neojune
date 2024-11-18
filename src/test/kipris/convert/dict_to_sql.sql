input => list[dict]

output => patent_company.sql 



INSERT INTO {table_name} ({', '.join(columns)}) 
            VALUES ({placeholders})
            ON DUPLICATE KEY UPDATE
            {additional_update_clause}
            {common_update_clause}
            legal_status_desc = VALUES(legal_status_desc),
            pub_num = VALUES(pub_num),
            pub_date = VALUES(pub_date)
            reg_no = VALUES(reg_no),
            reg_date = VALUES(reg_date),
            open_no = VALUES(open_no),
            open_date = VALUES(open_date),
            ;


INSERT INTO {table_name} ({', '.join(columns)}) 
            VALUES ({placeholders})
            ON DUPLICATE KEY UPDATE
            {additional_update_clause}
            {common_update_clause}
            legal_status_desc = VALUES(legal_status_desc),
            pub_num = VALUES(pub_num),
            pub_date = VALUES(pub_date)
            ;


INSERT INTO TB24_company_design (agent, appl_date, appl_no, applicant, applicant_id, image_path, inventor, ipr_code, legal_status_desc, open_date, open_no, pub_date, pub_num, reg_date, reg_no, serial_no, title) VALUES 
('최경수', '20140408', '3020140017534', '주식회사 파인메딕스|전성우', 2, 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e29e0b68f68d514bb0fedbb1325566a2d358de5f2bd287de10331b3d1887947c482a970947ddae1bf2bf9cda621bd8ba0d7223906319bd9903', '전성우', '30', '등록', None, None, '20141205', None, '20141201', '3007743290000', '1', '내시경시술용 핸들');

INSERT INTO TB24_company_patent (ipr_code, title, applicant_id, serial_no, applicant, main_ipc, appl_no, appl_date, open_no, open_date, reg_no, reg_date, pub_num, pub_date, legal_status_desc, abstract, image_path) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
legal_status_desc = VALUES(legal_status_desc),
pub_num = VALUES(pub_num),
pub_date = VALUES(pub_date)
        ;
        
('20', '디지탈 날염기', 5576, '1', '주식회사 메카트로', 'B41J 3/407', '2020020028364', '20020919', '3011244660000', '20210818', '3011244660000', '20210818', None, None, '거절', '본 고안은 디지털 날염기에 관한 것으로, ... 디지털 날염기를 제공한다. 디지털 날염기, 이송구동수단, 링크결합체, 인쇄감지센서, 자동승강조절수단', 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e22d01c5c32ba711cfdfd0c8a3560dfe3f5c0c0fb908b6de237d7cc48779f92f863537681dac20830b')


INSERT INTO TB24_company_patent 
(applicant_id, ipr_code, title, serial_no, applicant, main_ipc, appl_no, appl_date, open_no, open_date, reg_no, reg_date, pub_num, pub_date, legal_status_desc, abstract, image_path)
VALUES 
(5576, '20', '디지탈 날염기', '1', '주식회사 메카트로', 'B41J 3/407', '2020020028364', '2002-09-19', '3011244660000', '2021-08-18', '3011244660000', '2021-08-18', NULL, NULL, '거절',  '본 고안은 디지털 날염기에 관한 것으로, ... 디지털 날염기를 제공한다. 디지털 날염기, 이송구동수단, 링크결합체, 인쇄감지센서, 자동승강조절수단','http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e22d01c5c32ba711cfdfd0c8a3560dfe3f5c0c0fb908b6de237d7cc48779f92f863537681dac20830b'),
(5577, '20', '디지탈1 날염기', '2', '주식2회사 메카트로', 'B41J 3/407', '20200230028364', '2002-09-19', '30112444660000', '2021-08-18', '3011244660000', '2021-08-18', NULL, NULL, '거절',  '본 고안은 디지털 날염기에 관한 것으로, ... 디지털 날염기를 제공한다. 디지털 날염기, 이송구동수단, 링크결합체, 인쇄감지센서, 자동승강조절수단','http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e22d01c5c32ba711cfdfd0c8a3560dfe3f5c0c0fb908b6de237d7cc48779f92f863537681dac20830b');



INSERT INTO TB24_company_design (agent, appl_date, appl_no, applicant, applicant_id, image_path, inventor, ipr_code, legal_status_desc, open_date, open_no, pub_date, pub_num, reg_date, reg_no, serial_no, title)
VALUES
('최경수', '201340408', '30201400117534', '주식회사 파인메딕스|전성우', 2, 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e29e0b68f68d514bb0fedbb1325566a2d358de5f2bd287de10331b3d1887947c482a970947ddae1bf2bf9cda621bd8ba0d7223906319bd9903', '전성우', '30', '등록', Null, Null, '20141205', Null, '20141201', '3007743290000', '1', '내시경시술용 핸들');

INSERT INTO TB24_company_design (agent, appl_date, appl_no, applicant, applicant_id, image_path, inventor, ipr_code, legal_status_desc, open_date, open_no, pub_date, pub_num, reg_date, reg_no, serial_no, title)
VALUES
('최경수', '2013-04-08', '30201400117534', '주식회사 파인메딕스|전성우', 2, 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e29e0b68f68d514bb0fedbb1325566a2d358de5f2bd287de10331b3d1887947c482a970947ddae1bf2bf9cda621bd8ba0d7223906319bd9903', '전성우', '30', '등록', NULL, NULL, '2014-12-05', NULL, '2014-12-01', '3007743290000', '1', '내시경시술용 핸들');


/* ('최경수', '201420408', '30201400174517', '주식회사 파인메딕스|전성우', 2, 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e29e0b68f68d514bb0fedbb1325566a2d358de5f2bd287de10331b3d1887947c482a970947ddae1bf2bf74789afb4fa1d83bb97f3174dc9436', '전성우', '30', '등록', None, None, '20141205', None, '20141201', '3007743270000', '2', '내시경용 생검기구'),
('최경수', '201410408', '30201400173534', '주식회사 파인메딕스|전성우', 3, 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e29e0b68f68d514bb0fedbb1325566a2d358de5f2bd287de10331b3d1887947c482a970947ddae1bf2bf9cda621bd8ba0d7223906319bd9903', '전성우', '30', '등록', None, None, '20141205', None, '20141201', '3007743290000', '1', '내시경시술용 핸들'),
('최경수', '201450408', '30201400175517', '주식회사 파인메딕스|전성우', 3, 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e29e0b68f68d514bb0fedbb1325566a2d358de5f2bd287de10331b3d1887947c482a970947ddae1bf2bf74789afb4fa1d83bb97f3174dc9436', '전성우', '30', '등록', None, None, '20141205', None, '20141201', '3007743270000', '2', '내시경용 생검기구'); */


INSERT INTO TB24_company_design (agent, appl_date, appl_no, applicant, applicant_id, image_path, inventor, ipr_code, legal_status_desc, open_date, open_no, pub_date, pub_num, reg_date, reg_no, serial_no, title)
VALUES
('최경수', '2014-12-01', '3020140017534', '주식회사 파인메딕스|전성우', 2, 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e29e0b68f68d514bb0fedbb1325566a2d358de5f2bd287de10331b3d1887947c482a970947ddae1bf2bf9cda621bd8ba0d7223906319bd9903', '전성우', '30', '등록', Null, Null, '2014-12-01', Null, '2014-12-01', '3007743290000', '1', '내시경시술용 핸들');
/* ('최경수', '20140408', '3020140017517', '주식회사 파인메딕스|전성우', 2, 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e29e0b68f68d514bb0fedbb1325566a2d358de5f2bd287de10331b3d1887947c482a970947ddae1bf2bf74789afb4fa1d83bb97f3174dc9436', '전성우', '30', '등록', Null, Null, '20141205', Null, '20141201', '3007743270000', '2', '내시경용 생검기구'),
('최경수', '20140408', '3020140017534', '주식회사 파인메딕스|전성우', 3, 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e29e0b68f68d514bb0fedbb1325566a2d358de5f2bd287de10331b3d1887947c482a970947ddae1bf2bf9cda621bd8ba0d7223906319bd9903', '전성우', '30', '등록', Null, Null, '20141205', Null, '20141201', '3007743290000', '1', '내시경시술용 핸들'),
('최경수', '20140408', '3020140017517', '주식회사 파인메딕스|전성우', 3, 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e29e0b68f68d514bb0fedbb1325566a2d358de5f2bd287de10331b3d1887947c482a970947ddae1bf2bf74789afb4fa1d83bb97f3174dc9436', '전성우', '30', '등록', Null, Null, '20141205', Null, '20141201', '3007743270000', '2', '내시경용 생검기구'); */



INSERT INTO TB24_company_design (agent, appl_date, appl_no, applicant, applicant_id, image_path, inventor, ipr_code, legal_status_desc, open_date, open_no, pub_date, pub_num, reg_date, reg_no, serial_no, title)
VALUES
('최경수', '2014-04-08', '30201400127534', '주식회사 파인메딕스|전성우', 2, 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e29e0b68f68d514bb0fedbb1325566a2d358de5f2bd287de10331b3d1887947c482a970947ddae1bf2bf9cda621bd8ba0d7223906319bd9903', '전성우', '30', '등록', NULL, NULL, '2014-12-05', NULL, '2014-12-01', '3007743290000', '1', '내시경시술용 핸들'),
('최경수', '2014-04-08', '30201403017517', '주식회사 파인메딕스|전성우', 2, 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e29e0b68f68d514bb0fedbb1325566a2d358de5f2bd287de10331b3d1887947c482a970947ddae1bf2bf74789afb4fa1d83bb97f3174dc9436', '전성우', '30', '등록', NULL, NULL, '2014-12-05', NULL, '2014-12-01', '3007743270000', '2', '내시경용 생검기구'),
('최경수', '2014-04-08', '30201440517534', '주식회사 파인메딕스|전성우', 3, 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e29e0b68f68d514bb0fedbb1325566a2d358de5f2bd287de10331b3d1887947c482a970947ddae1bf2bf9cda621bd8ba0d7223906319bd9903', '전성우', '30', '등록', NULL, NULL, '2014-12-05', NULL, '2014-12-01', '3007743290000', '1', '내시경시술용 핸들'),
('최경수', '2014-04-08', '30201402017517', '주식회사 파인메딕스|전성우', 3, 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e29e0b68f68d514bb0fedbb1325566a2d358de5f2bd287de10331b3d1887947c482a970947ddae1bf2bf74789afb4fa1d83bb97f3174dc9436', '전성우', '30', '등록', NULL, NULL, '2014-12-05', NULL, '2014-12-01', '3007743270000', '2', '내시경용 생검기구');