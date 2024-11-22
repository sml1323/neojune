import streamlit as st
import pandas as pd
from io import BytesIO
from db_connection import fetch_data

def display_company_data():
    st.subheader("기업 데이터")
    # session_state 초기화 (없으면 1로 설정)
    if "page" not in st.session_state:
        st.session_state.page = 1  # 기본 페이지는 1
    if "biz_type" not in st.session_state:
        st.session_state.biz_type = "All"  # 기본 선택값은 "All"
    biz_type = st.sidebar.selectbox("Select Business Type", ["All", "법인", "개인"])
    
    # 필터가 변경될 때 첫 페이지로 이동
    if biz_type != st.session_state.get('biz_type', None):
        st.session_state.page = 1  # 첫 페이지로 리셋
        st.session_state.biz_type = biz_type  # 필터 상태 저장
        st.rerun()  # 페이지 갱신

   # 페이지네이션 변수 설정
    page_size = 50  # 페이지당 데이터 크기
    offset = (st.session_state.page - 1) * page_size  # OFFSET 계산

    company_query = f"SELECT biz_no, corp_no, biz_type, company_name FROM TB24_100 LIMIT {page_size} OFFSET {offset}" if biz_type == "All" else f"SELECT * FROM TB24_100 WHERE biz_type = '{biz_type}'"
    company_data = fetch_data(company_query)

    # 총 기업 데이터 건수 계산 (페이징을 위한)
    total_query = f"SELECT COUNT(*) FROM TB24_100" if biz_type == "All" else f"SELECT COUNT(*) FROM TB24_100 WHERE biz_type = '{biz_type}'"
    total_data = fetch_data(total_query)
    total_records = total_data.iloc[0, 0]
    total_pages = (total_records // page_size) + (1 if total_records % page_size > 0 else 0)  # 총 페이지 수 계산

    # 총 기업 데이터 수 문구 동적으로 변경
    if biz_type == "All":
        st.write(f"**전체** 기업 정보 데이터: {total_records:,}개")
    elif biz_type == "법인":
        st.write(f"**법인** 기업 정보 데이터: {total_records:,}개")
    elif biz_type == "개인":
        st.write(f"**개인** 기업 정보 데이터: {total_records:,}개")

    # 데이터프레임 표시
    paged_data_reset = company_data.reset_index(drop=True)
    paged_data_reset.index += (st.session_state.page - 1) * page_size + 1
    st.dataframe(paged_data_reset, height=700, use_container_width=True)

    # 페이지 슬라이더 범위 동적 설정
    page = st.sidebar.slider("Page", 1, total_pages, st.session_state.page)
    # 슬라이더 값이 변경되면 session_state.page 갱신
    if page != st.session_state.page:
        st.session_state.page = page
        st.rerun()  # 페이지 갱신

    # 기업 데이터 페이징 처리
    company_query = f"SELECT biz_no, corp_no, biz_type, company_name FROM TB24_100 LIMIT {page_size} OFFSET {(page - 1) * page_size}" if biz_type == "All" else f"SELECT * FROM TB24_100 WHERE biz_type = '{biz_type}' LIMIT {page_size} OFFSET {(page - 1) * page_size}"
    company_data = fetch_data(company_query)

    # 인덱스를 1부터 시작하도록 수정
    paged_data_reset = company_data.reset_index(drop=True)
    paged_data_reset.index += (page - 1) * page_size + 1  # 페이지 번호에 맞게 인덱스 조정

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
    num_buttons = len(page_buttons)
    
    # st.columns(num_buttons)로 열을 만들고, 각 열에 버튼 배치
    cols = st.columns(num_buttons)  # 페이지 버튼의 개수만큼 열을 만듦

    for idx, page_num in enumerate(page_buttons):
        with cols[idx]:
            # 버튼 간의 간격을 줄이기 위해 margin을 조정
            if st.button(page_num, key=page_num, use_container_width=False):  # 버튼 클릭 시
                if page_num == '◀' and st.session_state.page > 1:
                    st.session_state.page -= max_buttons  # 5개씩 이동
                elif page_num == '▶' and st.session_state.page + max_buttons <= total_pages:
                    st.session_state.page += max_buttons  # 5개씩 이동
                elif page_num.isdigit():
                    st.session_state.page = int(page_num)

                # 페이지 번호 클릭 후 새로고침 (데이터 갱신)
                st.rerun()  # 페이지 갱신

    # 다운로드 버튼
    st.download_button(
            label="📥 기업 데이터 다운로드", 
            data=convert_df_to_excel(paged_data_reset), 
            file_name=f"company_data.xlsx", 
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