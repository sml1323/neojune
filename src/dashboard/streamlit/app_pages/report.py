import streamlit as st
import plotly.express as px
from datetime import datetime, timedelta
from db_connection import fetch_data

def display_report():
    st.subheader("기업 Report 요약")
    st.markdown("한달 전 데이터 대비")
    st.markdown("<br>", unsafe_allow_html=True) 

    # 오늘 날짜, 한달 전 날짜, 하루 전 날짜 계산
    today = datetime.today().strftime('%Y-%m-%d')
    one_month_ago = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')

    # 기업 특허, 디자인, 상표 통계 요약 (한 달 전과 비교)
    total_patents_query = f"""
        SELECT 
            COUNT(*) AS total_patents,
            SUM(CASE WHEN appl_date >= '{one_month_ago}' THEN 1 ELSE 0 END) AS recent_patents
        FROM TB24_company_patent
        UNION ALL
        SELECT 
            COUNT(*) AS total_designs,
            SUM(CASE WHEN appl_date >= '{one_month_ago}' THEN 1 ELSE 0 END) AS recent_designs
        FROM TB24_company_design
        UNION ALL
        SELECT 
            COUNT(*) AS total_trademarks,
            SUM(CASE WHEN appl_date >= '{one_month_ago}' THEN 1 ELSE 0 END) AS recent_trademarks
        FROM TB24_company_trademark
    """

    total_data = fetch_data(total_patents_query)
    total_patents = total_data.iloc[0, 0]
    recent_patents = total_data.iloc[0, 1]
    total_designs = total_data.iloc[1, 0]
    recent_designs = total_data.iloc[1, 1]
    total_trademarks = total_data.iloc[2, 0]
    recent_trademarks = total_data.iloc[2, 1]

    # 기업 요약 카드 표시
    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric("총 특허/실용신안 수", f"{int(total_patents):,} 건", f"{int(recent_patents):,} 건")
    col2.metric("총 디자인 수", f"{int(total_designs):,} 건", f"{int(recent_designs):,} 건")
    col3.metric("총 상표 수", f"{int(total_trademarks):,} 건", f"{int(recent_trademarks):,} 건")
    
    st.markdown("<br>", unsafe_allow_html=True) 

    # 기업 출원 추세 
    st.subheader("기업 출원 수")
    # 한달 전 추세
    date_query_month = f"""
        SELECT appl_date, 
            SUM(CASE WHEN ipr_code IN ('10', '20') THEN 1 ELSE 0 END) as patent_count,  -- 특허
            SUM(CASE WHEN ipr_code = '30' THEN 1 ELSE 0 END) as design_count,           -- 디자인
            SUM(CASE WHEN ipr_code = '40' THEN 1 ELSE 0 END) as trademark_count         -- 상표
        FROM (
            SELECT appl_date, ipr_code FROM TB24_company_patent
            UNION ALL
            SELECT appl_date, ipr_code FROM TB24_company_design
            UNION ALL
            SELECT appl_date, ipr_code FROM TB24_company_trademark
        ) AS company_data
        WHERE appl_date >= '{one_month_ago}'  -- 최근 한 달 데이터만
        GROUP BY appl_date
        ORDER BY appl_date
    """
    date_data_month = fetch_data(date_query_month)

    # 기업 출원건수 추세 라인 차트 생성 (한달 간)
    line_chart_month = px.line()
    line_chart_month.add_scatter(x=date_data_month['appl_date'], y=date_data_month['patent_count'], mode='lines', name='특허/실용신안')
    line_chart_month.add_scatter(x=date_data_month['appl_date'], y=date_data_month['design_count'], mode='lines', name='디자인')
    line_chart_month.add_scatter(x=date_data_month['appl_date'], y=date_data_month['trademark_count'], mode='lines', name='상표')

    line_chart_month.update_layout(xaxis_title="출원일", yaxis_title="출원 건수", legend_title="출원 종류", title="기업 등록 추세 (한달 간)", title_x=0.4)

    # 각 트레이스의 레이블 변경
    line_chart_month.update_traces(name='특허/실용신안 수', selector=dict(name='patent_count'))
    line_chart_month.update_traces(name='디자인 수', selector=dict(name='design_count'))
    line_chart_month.update_traces(name='상표 수', selector=dict(name='trademark_count'))

    st.plotly_chart(line_chart_month, use_container_width=True)

    st.markdown("<br><hr><br>", unsafe_allow_html=True)

    # 대학교 Report 요약
    st.subheader("대학교 Report 요약")
    st.markdown("한달 전 데이터 대비")
    st.markdown("<br>", unsafe_allow_html=True) 

    # 대학교 특허, 디자인, 상표 통계 요약 (한달 전과 비교)
    university_patents_query = f"""
        SELECT 
            COUNT(*) AS total_patents,
            SUM(CASE WHEN appl_date >= '{one_month_ago}' THEN 1 ELSE 0 END) AS recent_patents
        FROM TB24_university_patent
        UNION ALL
        SELECT 
            COUNT(*) AS total_designs,
            SUM(CASE WHEN appl_date >= '{one_month_ago}' THEN 1 ELSE 0 END) AS recent_designs
        FROM TB24_university_design
        UNION ALL
        SELECT 
            COUNT(*) AS total_trademarks,
            SUM(CASE WHEN appl_date >= '{one_month_ago}' THEN 1 ELSE 0 END) AS recent_trademarks
        FROM TB24_university_trademark
    """

    university_data = fetch_data(university_patents_query)
    university_total_patents = university_data.iloc[0, 0]
    university_recent_patents = university_data.iloc[0, 1]
    university_total_designs = university_data.iloc[1, 0]
    university_recent_designs = university_data.iloc[1, 1]
    university_total_trademarks = university_data.iloc[2, 0]
    university_recent_trademarks = university_data.iloc[2, 1]

    # 대학교 요약 카드 표시
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("총 특허/실용신안 수", f"{int(university_total_patents):,} 건", f"{int(university_recent_patents):,} 건")
    col2.metric("총 디자인 수", f"{int(university_total_designs):,} 건", f"{int(university_recent_designs):,} 건")
    col3.metric("총 상표 수", f"{int(university_total_trademarks):,} 건", f"{int(university_recent_trademarks):,} 건")

    st.markdown("<br>", unsafe_allow_html=True)

    # 대학교 출원 추세
    st.subheader("대학교 출원 수")
    # 한달 전 추세
    university_date_query_month = f"""
        SELECT appl_date, 
            SUM(CASE WHEN ipr_code IN ('10', '20') THEN 1 ELSE 0 END) as patent_count,  -- 특허
            SUM(CASE WHEN ipr_code = '30' THEN 1 ELSE 0 END) as design_count,           -- 디자인
            SUM(CASE WHEN ipr_code = '40' THEN 1 ELSE 0 END) as trademark_count         -- 상표
        FROM (
            SELECT appl_date, ipr_code FROM TB24_university_patent
            UNION ALL
            SELECT appl_date, ipr_code FROM TB24_university_design
            UNION ALL
            SELECT appl_date, ipr_code FROM TB24_university_trademark
        ) AS university_data
        WHERE appl_date >= '{one_month_ago}'  -- 최근 한 달 데이터만
        GROUP BY appl_date
        ORDER BY appl_date
    """
    university_date_data_month = fetch_data(university_date_query_month)

    # 대학교 출원 추세 라인 차트 생성 (한달 간)
    university_line_chart_month = px.line()
    university_line_chart_month.add_scatter(x=university_date_data_month['appl_date'], y=university_date_data_month['patent_count'], mode='lines', name='특허/실용신안')
    university_line_chart_month.add_scatter(x=university_date_data_month['appl_date'], y=university_date_data_month['design_count'], mode='lines', name='디자인')
    university_line_chart_month.add_scatter(x=university_date_data_month['appl_date'], y=university_date_data_month['trademark_count'], mode='lines', name='상표')

    university_line_chart_month.update_layout(xaxis_title="출원일", yaxis_title="출원 건수", legend_title="출원 종류", title="대학교 출원 추세 (한달 간)", title_x=0.4)

    # 각 트레이스의 레이블 변경
    university_line_chart_month.update_traces(name='특허/실용신안 수', selector=dict(name='patent_count'))
    university_line_chart_month.update_traces(name='디자인 수', selector=dict(name='design_count'))
    university_line_chart_month.update_traces(name='상표 수', selector=dict(name='trademark_count'))

    st.plotly_chart(university_line_chart_month, use_container_width=True)