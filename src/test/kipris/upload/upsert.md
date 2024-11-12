## input => list[dict]
```python
design = [{
    'agent': '최경수',
    'appl_date': '20140408',
    'appl_no': '3020140017534',
    'applicant': '주식회사 파인메딕스|전성우',
    'applicant_id': 2,
    'image_path': 'http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e29e0b68f68d514bb0fedbb1325566a2d358de5f2bd287de10331b3d1887947c482a970947ddae1bf2bf9cda621bd8ba0d7223906319bd9903',
    'inventor': '전성우',
    'ipr_code': '30',
    # 'ipr_seq': '',
    'legal_status_desc': '등록',
    'open_date': None,
    'open_no': None,
    'pub_date': '20141205',
    'pub_num': None,
    'reg_date': '20141201',.jo
    'reg_no': '3007743290000',
    'serial_no': '1',
    'title': '내시경시술용 핸들'
},
]
```


## output => patent_company.sql 
```sql
INSERT INTO TB24_company_design 



```


```sql

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
```