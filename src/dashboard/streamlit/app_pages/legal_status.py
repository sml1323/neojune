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
    
    # session_state 초기화 (없으면 1로 설정)
    if "page" not in st.session_state:
        st.session_state.page = 1
    if "selected_status" not in st.session_state:
        st.session_state.selected_status = selected_status 
    
    # 필터가 변경될 때 첫 페이지로 이동
    if selected_status != st.session_state.get('selected_status', None):
        st.session_state.page = 1  
        st.session_state.selected_status = selected_status 
        st.rerun() 
    
    # 페이지네이션 변수 설정
    page_size = 50  # 페이지당 데이터 크기
    offset = (st.session_state.page - 1) * page_size 

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
    LIMIT {page_size} OFFSET {offset} 
    """

    # 데이터 불러오기
    legal_status_data = fetch_legal_status_data(legal_status_query)

    # 총 데이터 건수 (페이징을 위한)
    total_query = f"""
    SELECT COUNT(*) 
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
    """
    total_data = fetch_legal_status_data(total_query)
    total_records = total_data.iloc[0, 0]
    total_pages = (total_records // page_size) + (1 if total_records % page_size > 0 else 0)  # 총 페이지 수 계산
    
    # 필터링된 데이터 표시
    if legal_status_data.shape[0] > 0:
        st.write(f"**{selected_status} 상태 데이터**")
        
        start_index = (st.session_state.page - 1) * page_size + 1
        legal_status_data_reset = legal_status_data.reset_index(drop=True)
        legal_status_data_reset.index = range(start_index, start_index + len(legal_status_data_reset))
        
        st.dataframe(legal_status_data_reset.rename(columns={'applicant': '출원인', 'appl_no': '출원번호', 
                                                            'appl_date': '출원일', 'ipr_code': '산업재산권 코드', 
                                                            'legal_status_desc': '법적 상태', 'pub_date': '변경일'}), 
                     use_container_width=True)
        
        # 페이지 슬라이더 범위 동적 설정
        page = st.sidebar.slider("Page", 1, total_pages, st.session_state.page)
        # 슬라이더 값이 변경되면 session_state.page 갱신
        if page != st.session_state.page:
            st.session_state.page = page
            st.rerun()  # 페이지 갱신
        
        # 페이지 번호 표시 (◀ 1 2 3 4 5 ▶ 형태로)
        total_pages = max(total_pages, 1)  # 최소 1페이지로 설정 (페이지가 없을 경우 대비)

        # 페이지 버튼 스타일 CSS 추가
        st.markdown(
            """
            <style>
            .stButton>button {
                width: 45px !important;
                height: 30px !important;
                font-size: 8px !important;
                margin: 0px !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # 가로로 페이지 버튼 배치
        num_buttons = 5
        start_page = max(1, st.session_state.page - num_buttons // 2)
        end_page = min(start_page + num_buttons - 1, total_pages)

        # 페이지 버튼들을 표시하기 위한 리스트
        page_buttons = []
        if start_page > 1:
            page_buttons.append('◀')  # 이전 페이지 버튼
        for i in range(start_page, end_page + 1):
            page_buttons.append(str(i))
        if end_page < total_pages:
            page_buttons.append('▶')  # 다음 페이지 버튼

        # 가로로 페이지 버튼 배치
        cols = st.columns(len(page_buttons))

        for idx, page_num in enumerate(page_buttons):
            with cols[idx]:
                if st.button(page_num, key=page_num, use_container_width=False):
                    if page_num == '◀' and st.session_state.page > 1:
                        st.session_state.page -= num_buttons
                    elif page_num == '▶' and st.session_state.page + num_buttons <= total_pages:
                        st.session_state.page += num_buttons
                    elif page_num.isdigit():
                        st.session_state.page = int(page_num)

                    # 페이지 번호 클릭 후 새로고침 (데이터 갱신)
                    st.rerun()  # 페이지 갱신