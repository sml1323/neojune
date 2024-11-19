import streamlit as st
import pandas as pd
from io import BytesIO
from db_connection import fetch_data

# 대학 데이터 페이지 함수
def display_university_data():
    st.subheader("대학교 데이터")
    # session_state 초기화 (없으면 1로 설정)
    if "page" not in st.session_state:
        st.session_state.page = 1  # 기본 페이지는 1
        
    # 페이지네이션 변수 설정
    page_size = 50  # 페이지당 데이터 크기
    offset = (st.session_state.page - 1) * page_size  # OFFSET 계산

    university_query = f"SELECT biz_no, corp_no, applicant FROM TB24_110 LIMIT {page_size} OFFSET {offset}" 
    university_data = fetch_data(university_query)

    # 총 대학교 데이터 건수 계산 (페이징을 위한)
    total_query = f"SELECT COUNT(*) FROM TB24_110" 
    total_data = fetch_data(total_query)
    total_records = total_data.iloc[0, 0]
    total_pages = (total_records // page_size) + (1 if total_records % page_size > 0 else 0)  # 총 페이지 수 계산

    # 대학교 데이터 수 표시
    st.write(f"전체 대학교 데이터: {total_records:,}개")

    # 페이지 슬라이더 범위 동적 설정
    page = st.sidebar.slider("Page", 1, total_pages, st.session_state.page)

    # 페이지 번호가 변경되면 session_state.page 갱신
    if page != st.session_state.page:
        st.session_state.page = page
        st.rerun()  # 페이지 갱신

    # 대학교 데이터 페이징 처리
    university_query = f"SELECT biz_no, corp_no, applicant FROM TB24_110 LIMIT {page_size} OFFSET {(page - 1) * page_size}" 
    university_data = fetch_data(university_query)

    # 인덱스를 1부터 시작하도록 수정
    paged_data_reset = university_data.reset_index(drop=True)
    paged_data_reset.index += (page - 1) * page_size + 1  # 페이지 번호에 맞게 인덱스 조정

    # 데이터프레임 표시
    st.dataframe(paged_data_reset, height=700, use_container_width=True)

    # 페이지 번호 표시 (◀ 1 2 3 4 5 ▶ 형태로)
    total_pages = max(total_pages, 1)  # 최소 1페이지로 설정 (페이지가 없을 경우 대비)
    
    # 페이지 번호를 고정 5개로 설정
    max_buttons = 5
    start_page = max(1, st.session_state.page - max_buttons // 2)
    end_page = min(start_page + max_buttons - 1, total_pages)

    # 페이지 버튼들을 표시하기 위한 리스트
    page_buttons = []
    if start_page > 1:
        page_buttons.append('◀')  # 이전 페이지 버튼
    for i in range(start_page, end_page + 1):
        page_buttons.append(str(i))
    if end_page < total_pages:
        page_buttons.append('▶')  # 다음 페이지 버튼

    # 페이지 버튼 스타일 CSS 추가
    st.markdown(
    """
    <style>
    .stButton>button {
        width: 45px !important;  /* 너비 고정 */
        height: 30px !important;
        font-size: 12px !important;
        margin: 1px !important;
    }
    .stButton>button:hover {
        background-color: #52d7ca;  /* Hover 시 배경 색상 */
    }
    </style>
    """,
    unsafe_allow_html=True
)

    # 가로로 페이지 버튼 배치
    num_buttons = len(page_buttons)

    # st.columns(num_buttons)로 열을 만들고, 각 열에 버튼 배치
    cols = st.columns(num_buttons)  # 페이지 버튼의 개수만큼 열을 만듦

    for idx, page_num in enumerate(page_buttons):
        with cols[idx]:
            if st.button(page_num, key=page_num, use_container_width=False):  # 버튼 클릭 시
                if page_num == '◀' and st.session_state.page > 1:
                    st.session_state.page -= max_buttons  # 5개씩 이동
                elif page_num == '▶' and st.session_state.page + max_buttons <= total_pages:
                    st.session_state.page += max_buttons  # 5개씩 이동
                elif page_num.isdigit():
                    st.session_state.page = int(page_num)

                # 페이지 번호 클릭 후 새로고침 (데이터 갱신)
                st.rerun()  # 페이지 갱신

    st.download_button(
            label="📥 대학교 데이터 다운로드", 
            data=convert_df_to_excel(paged_data_reset), 
            file_name=f"university_data.xlsx", 
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

# 엑셀 파일로 변환하는 함수
def convert_df_to_excel(df):
    """DataFrame을 엑셀 형식으로 변환하여 반환하는 함수"""
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)
        writer.close()
    output.seek(0)
    return output.read()