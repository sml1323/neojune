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