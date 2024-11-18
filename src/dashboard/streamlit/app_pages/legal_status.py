import streamlit as st
import pandas as pd
from io import BytesIO
from datetime import datetime
from db_connection import fetch_data

@st.cache_data
def fetch_legal_status_data(legal_status_query):
    return fetch_data(legal_status_query)

def display_legal_status_data(): 
    st.subheader("산업재산권 법적 상태 데이터")

    # 오늘 날짜 계산
    today = datetime.today().strftime('%Y-%m-%d')
    
    # 법적 상태 종류
    status_choices = ['등록', '거절', '소멸', '포기', '공개', '취하']
    
    # 법적 상태 검색란
    selected_status = st.selectbox(f"📅 **{today} 기준 법적 상태 조회**", status_choices)
    
    # 법적 상태 검색 쿼리
    legal_status_query = f"""
    SELECT applicant, appl_no, appl_date, ipr_code, legal_status_desc, pub_date
    FROM (
        SELECT applicant, appl_no, appl_date, ipr_code, legal_status_desc, pub_date
        FROM TB24_company_patent
        WHERE legal_status_desc = '{selected_status}'
        UNION ALL
        SELECT applicant, appl_no, appl_date, ipr_code, legal_status_desc, pub_date
        FROM TB24_company_design
        WHERE legal_status_desc = '{selected_status}'
        UNION ALL
        SELECT applicant, appl_no, appl_date, ipr_code, legal_status_desc, pub_date
        FROM TB24_company_trademark
        WHERE legal_status_desc = '{selected_status}'
    ) AS legal_status_data
    ORDER BY pub_date DESC
    """
    
    # 데이터 불러오기
    legal_status_data = fetch_legal_status_data(legal_status_query)
    
    # 필터링된 데이터 표시
    if legal_status_data.shape[0] > 0:
        st.write(f"**{selected_status} 상태 데이터**")
        
        legal_status_data_reset = legal_status_data.reset_index(drop=True)
        legal_status_data_reset.index += 1  # 인덱스를 1부터 시작하도록 조정
        
        st.dataframe(legal_status_data_reset.rename(columns={'applicant': '출원인', 'appl_no': '출원번호', 
                                                            'appl_date': '출원일', 'ipr_code': '산업재산권 코드', 
                                                            'legal_status_desc': '법적 상태', 'pub_date': '변경일'}), 
                     use_container_width=True)
        
        st.download_button(
            label="📥 법적 상태 데이터 다운로드", 
            data=convert_df_to_excel(legal_status_data_reset), 
            file_name=f"legal_status_data_{today}.xlsx", 
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        
    else:
        st.write(f"**{selected_status}** 상태 변경된 데이터가 없습니다.")

# 엑셀 파일로 변환하는 함수
def convert_df_to_excel(df):
    """DataFrame을 엑셀 형식으로 변환하여 반환하는 함수"""
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)
        writer.close()
    output.seek(0)
    return output.read()