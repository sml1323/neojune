import streamlit as st
from streamlit_option_menu import option_menu
from db_connection import fetch_data
from app_pages import dashboard, company_data, company_analyze, university_data, legal_status, report

# Streamlit 설정
st.set_page_config(page_title="산업재산권 Dashboard", layout="wide")
st.title("📊 Dashboard 📊")
st.sidebar.header("Select Options")

# 페이지 네비게이션 처리
def get_paged_data(data, page_size=30):
    total_pages = (len(data) // page_size) + (1 if len(data) % page_size != 0 else 0)  # 전체 페이지 수 계산
    if 'page' not in st.session_state:
        st.session_state.page = 1  # 기본 페이지 번호는 1

    # 페이지 번호 갱신
    query_params = st.query_params
    if 'page' in query_params:
        new_page = int(query_params['page'][0])
        if new_page != st.session_state.page:
            st.session_state.page = new_page
            st.rerun()  # 페이지 변경 후 새로고침 (데이터 갱신)

    # 페이징된 데이터 반환
    start_idx = (st.session_state.page - 1) * page_size
    end_idx = start_idx + page_size
    paged_data = data[start_idx:end_idx]

    return paged_data, st.session_state.page, total_pages

# 사이드바 페이지 선택
with st.sidebar:
    page = option_menu(
            "",  # 메뉴 제목(생략)
            ["Dashboard", "법적 상태", "기업 분석", "Report", "기업", "대학교"],  
            icons=['house', 'bi bi-book', 'bi bi-pie-chart', 'bi bi-bar-chart-line', 'bi bi-building', 'bi bi-mortarboard'],  # 아이콘 추가
            menu_icon="app-indicator",  # 사이드바 상단 아이콘
            default_index=0,  # 기본 선택값
            styles={
                "container": {"padding": "4px!important", "background-color": "#fafafa"},
                "icon": {"color": "black", "font-size": "22px"},
                "nav-link": {
                    "font-size": "14px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#fafafa"
                },
                "nav-link-selected": {"background-color": "#52d7ca"},
            }
        )

if page == "Dashboard":
    dashboard.display_dashboard_summary()
elif page == "기업":
    company_data.display_company_data()
elif page == "기업 분석":
    company_analyze.display_company_analyze()
elif page == "대학교":
    university_data.display_university_data()
elif page == "법적 상태":  
    legal_status.display_legal_status_data()  
elif page == "Report":
    report.display_report()