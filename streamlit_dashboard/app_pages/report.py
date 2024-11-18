import streamlit as st
import plotly.express as px
from datetime import datetime, timedelta
from db_connection import fetch_data

def display_report():
    st.subheader("기업 Report 요약(한 달)")

    # 오늘 날짜, 한달 전 날짜, 하루 전 날짜 계산
    today = datetime.today().strftime('%Y-%m-%d')
    one_month_ago = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')
    one_day_ago = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')

    # 기업 특허, 디자인, 상표 통계 요약 (한 달 전과 비교)
    total_patents_query = f"""
        SELECT 
            COUNT(*) AS total_patents,
            SUM(CASE WHEN pub_date >= '{one_month_ago}' THEN 1 ELSE 0 END) AS recent_patents
        FROM TB24_company_patent
        UNION ALL
        SELECT 
            COUNT(*) AS total_designs,
            SUM(CASE WHEN pub_date >= '{one_month_ago}' THEN 1 ELSE 0 END) AS recent_designs
        FROM TB24_company_design
        UNION ALL
        SELECT 
            COUNT(*) AS total_trademarks,
            SUM(CASE WHEN pub_date >= '{one_month_ago}' THEN 1 ELSE 0 END) AS recent_trademarks
        FROM TB24_company_trademark
    """

    total_applicants_query = f"""
        SELECT 
            COUNT(DISTINCT applicant) AS total_applicants,
            COUNT(DISTINCT CASE WHEN pub_date >= '{one_month_ago}' THEN applicant ELSE NULL END) AS recent_applicants
        FROM TB24_company_patent
    """
    
    total_data = fetch_data(total_patents_query)
    total_patents = total_data.iloc[0, 0]
    recent_patents = total_data.iloc[0, 1]
    total_designs = total_data.iloc[1, 0]
    recent_designs = total_data.iloc[1, 1]
    total_trademarks = total_data.iloc[2, 0]
    recent_trademarks = total_data.iloc[2, 1]
    
    total_applicants_data = fetch_data(total_applicants_query) 
    total_applicants = total_applicants_data.iloc[0, 0]
    recent_applicants = total_applicants_data.iloc[0, 1]

    # 증감 계산 (최근 30일 동안의 등록 수)
    change_patents = recent_patents - (total_patents - recent_patents)
    change_designs = recent_designs - (total_designs - recent_designs)
    change_trademarks = recent_trademarks - (total_trademarks - recent_trademarks)
    change_applicants = recent_applicants - (total_applicants - recent_applicants)
    
    # 하루 전 데이터 가져오기
    yesterday_patents_query = f"""
        SELECT 
            COUNT(*) AS yesterday_patents
        FROM TB24_company_patent
        WHERE pub_date >= '{one_day_ago}' AND pub_date < '{today}'
    """
    
    yesterday_designs_query = f"""
        SELECT 
            COUNT(*) AS yesterday_designs
        FROM TB24_company_design
        WHERE pub_date >= '{one_day_ago}' AND pub_date < '{today}'
    """
    
    yesterday_trademarks_query = f"""
        SELECT 
            COUNT(*) AS yesterday_trademarks
        FROM TB24_company_trademark
        WHERE pub_date >= '{one_day_ago}' AND pub_date < '{today}'
    """
    
    yesterday_applicants_query = f"""
        SELECT 
            COUNT(DISTINCT applicant) AS yesterday_applicants
        FROM TB24_company_patent
        WHERE pub_date >= '{one_day_ago}' AND pub_date < '{today}'
    """

    # 하루 전 데이터 가져오기
    yesterday_patents_data = fetch_data(yesterday_patents_query)
    yesterday_patents = yesterday_patents_data.iloc[0, 0]

    yesterday_designs_data = fetch_data(yesterday_designs_query)
    yesterday_designs = yesterday_designs_data.iloc[0, 0]

    yesterday_trademarks_data = fetch_data(yesterday_trademarks_query)
    yesterday_trademarks = yesterday_trademarks_data.iloc[0, 0]

    yesterday_applicants_data = fetch_data(yesterday_applicants_query)
    yesterday_applicants = yesterday_applicants_data.iloc[0, 0]

    # 하루 전 대비 증감 계산
    change_patents_yesterday = recent_patents - yesterday_patents
    change_designs_yesterday = recent_designs - yesterday_designs
    change_trademarks_yesterday = recent_trademarks - yesterday_trademarks
    change_applicants_yesterday = recent_applicants - yesterday_applicants

    # 기업 요약 카드 표시
    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric("총 특허/실용신안 수", f"{int(total_patents):,} 건", f"{int(change_patents):,} 건")
    col2.metric("총 디자인 수", f"{int(total_designs):,} 건", f"{int(change_designs):,} 건")
    col3.metric("총 상표 수", f"{int(total_trademarks):,} 건", f"{int(change_trademarks):,} 건")
    col4.metric("총 출원인 수", f"{int(total_applicants):,} 건", f"{int(change_applicants):,} 건")
    
    st.markdown("<br>", unsafe_allow_html=True) 

    # 기업 등록 추세 (특허, 디자인, 상표)
    st.subheader("기업 등록 추세")
    # 한 달 전 추세
    date_query_month = f"""
        SELECT pub_date, 
            SUM(CASE WHEN ipr_code IN ('10', '20') THEN 1 ELSE 0 END) as patent_count,  -- 특허
            SUM(CASE WHEN ipr_code = '30' THEN 1 ELSE 0 END) as design_count,           -- 디자인
            SUM(CASE WHEN ipr_code = '40' THEN 1 ELSE 0 END) as trademark_count         -- 상표
        FROM (
            SELECT pub_date, ipr_code FROM TB24_company_patent
            UNION ALL
            SELECT pub_date, ipr_code FROM TB24_company_design
            UNION ALL
            SELECT pub_date, ipr_code FROM TB24_company_trademark
        ) AS company_data
        WHERE pub_date >= '{one_month_ago}'  -- 최근 한 달 데이터만
        GROUP BY pub_date
        ORDER BY pub_date
    """
    date_data_month = fetch_data(date_query_month)

    # 하루 전 추세
    date_query_day = f"""
        SELECT pub_date, 
            SUM(CASE WHEN ipr_code IN ('10', '20') THEN 1 ELSE 0 END) as patent_count,  -- 특허
            SUM(CASE WHEN ipr_code = '30' THEN 1 ELSE 0 END) as design_count,           -- 디자인
            SUM(CASE WHEN ipr_code = '40' THEN 1 ELSE 0 END) as trademark_count         -- 상표
        FROM (
            SELECT pub_date, ipr_code FROM TB24_company_patent
            UNION ALL
            SELECT pub_date, ipr_code FROM TB24_company_design
            UNION ALL
            SELECT pub_date, ipr_code FROM TB24_company_trademark
        ) AS company_data
        WHERE pub_date >= '{one_day_ago}'  -- 하루 전 데이터만
        GROUP BY pub_date
        ORDER BY pub_date
    """
    date_data_day = fetch_data(date_query_day)

    # 기업 등록 추세 라인 차트 생성 (한 달 간)
    line_chart_month = px.line()
    line_chart_month.add_scatter(x=date_data_month['pub_date'], y=date_data_month['patent_count'], mode='lines', name='한 달 전 특허/실용신안')
    line_chart_month.add_scatter(x=date_data_month['pub_date'], y=date_data_month['design_count'], mode='lines', name='한 달 전 디자인')
    line_chart_month.add_scatter(x=date_data_month['pub_date'], y=date_data_month['trademark_count'], mode='lines', name='한 달 전 상표')

    line_chart_month.update_layout(
        xaxis_title="등록일", 
        yaxis_title="등록 건수", 
        legend_title="등록 종류", 
        title="기업 등록 추세 (한 달 간)", 
        title_x=0.4  # 제목 가운데 정렬
    )
    # 각 트레이스의 레이블 변경
    line_chart_month.update_traces(name='특허/실용신안 수', selector=dict(name='patent_count'))
    line_chart_month.update_traces(name='디자인 수', selector=dict(name='design_count'))
    line_chart_month.update_traces(name='상표 수', selector=dict(name='trademark_count'))

    # 기업 등록 추세 라인 차트 생성 (1일 간)
    line_chart_day = px.line()
    line_chart_day.add_scatter(x=date_data_day['pub_date'], y=date_data_day['patent_count'], mode='lines', name='하루 전 특허/실용신안', line=dict(dash='dash'))
    line_chart_day.add_scatter(x=date_data_day['pub_date'], y=date_data_day['design_count'], mode='lines', name='하루 전 디자인', line=dict(dash='dash'))
    line_chart_day.add_scatter(x=date_data_day['pub_date'], y=date_data_day['trademark_count'], mode='lines', name='하루 전 상표', line=dict(dash='dash'))

    line_chart_day.update_layout(xaxis_title="등록일", yaxis_title="등록 건수", legend_title="등록 종류", title="기업 등록 추세 (1일 간)", title_x=0.4)

    line_chart_day.update_traces(name='특허/실용신안 수',  selector=dict(name='patent_count'))
    line_chart_day.update_traces(name='디자인 수', selector=dict(name='design_count'))
    line_chart_day.update_traces(name='상표 수', selector=dict(name='trademark_count'))

    st.plotly_chart(line_chart_day, use_container_width=True)
    st.plotly_chart(line_chart_month, use_container_width=True)

    st.markdown("<br><hr><br>", unsafe_allow_html=True)

    # 대학교 Report 요약
    st.subheader("대학교 Report 요약(한 달)")

    # 대학교 특허, 디자인, 상표 통계 요약 (한 달 전과 비교)
    university_patents_query = f"""
        SELECT 
            COUNT(*) AS total_patents,
            SUM(CASE WHEN pub_date >= '{one_month_ago}' THEN 1 ELSE 0 END) AS recent_patents
        FROM TB24_university_patent
        UNION ALL
        SELECT 
            COUNT(*) AS total_designs,
            SUM(CASE WHEN pub_date >= '{one_month_ago}' THEN 1 ELSE 0 END) AS recent_designs
        FROM TB24_university_design
        UNION ALL
        SELECT 
            COUNT(*) AS total_trademarks,
            SUM(CASE WHEN pub_date >= '{one_month_ago}' THEN 1 ELSE 0 END) AS recent_trademarks
        FROM TB24_university_trademark
    """

    university_applicants_query = f"""
        SELECT 
            COUNT(DISTINCT applicant) AS total_applicants,
            COUNT(DISTINCT CASE WHEN pub_date >= '{one_month_ago}' THEN applicant ELSE NULL END) AS recent_applicants
        FROM TB24_university_patent
    """

    university_data = fetch_data(university_patents_query)
    university_total_patents = university_data.iloc[0, 0]
    university_recent_patents = university_data.iloc[0, 1]
    university_total_designs = university_data.iloc[1, 0]
    university_recent_designs = university_data.iloc[1, 1]
    university_total_trademarks = university_data.iloc[2, 0]
    university_recent_trademarks = university_data.iloc[2, 1]

    university_applicants_data = fetch_data(university_applicants_query)
    university_total_applicants = university_applicants_data.iloc[0, 0]
    university_recent_applicants = university_applicants_data.iloc[0, 1]

    # 증감 계산 (최근 30일 동안의 등록 수)
    university_change_patents = university_recent_patents - (university_total_patents - university_recent_patents)
    university_change_designs = university_recent_designs - (university_total_designs - university_recent_designs)
    university_change_trademarks = university_recent_trademarks - (university_total_trademarks - university_recent_trademarks)
    university_change_applicants = university_recent_applicants - (university_total_applicants - university_recent_applicants)

    # 대학교 요약 카드 표시
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("총 특허/실용신안 수", f"{int(university_total_patents):,} 건", f"{int(university_change_patents):,} 건")
    col2.metric("총 디자인 수", f"{int(university_total_designs):,} 건", f"{int(university_change_designs):,} 건")
    col3.metric("총 상표 수", f"{int(university_total_trademarks):,} 건", f"{int(university_change_trademarks):,} 건")
    col4.metric("총 출원인 수", f"{int(university_total_applicants):,} 건", f"{int(university_change_applicants):,} 건")

    st.markdown("<br>", unsafe_allow_html=True)

    # 대학교 등록 추세 (특허, 디자인, 상표)
    st.subheader("대학교 등록 추세")
    university_date_query = f"""
        SELECT pub_date, 
            SUM(CASE WHEN ipr_code IN ('10', '20') THEN 1 ELSE 0 END) as patent_count,  -- 특허
            SUM(CASE WHEN ipr_code = '30' THEN 1 ELSE 0 END) as design_count,           -- 디자인
            SUM(CASE WHEN ipr_code = '40' THEN 1 ELSE 0 END) as trademark_count         -- 상표
        FROM (
            SELECT pub_date, ipr_code FROM TB24_university_patent
            UNION ALL
            SELECT pub_date, ipr_code FROM TB24_university_design
            UNION ALL
            SELECT pub_date, ipr_code FROM TB24_university_trademark
        ) AS university_data
        WHERE pub_date >= '{one_month_ago}'  -- 최근 한 달 데이터만
        GROUP BY pub_date
        ORDER BY pub_date
    """
    university_date_data = fetch_data(university_date_query)

    # 하루 전 데이터 가져오기
    university_date_query_day = f"""
        SELECT pub_date, 
            SUM(CASE WHEN ipr_code IN ('10', '20') THEN 1 ELSE 0 END) as patent_count,  -- 특허
            SUM(CASE WHEN ipr_code = '30' THEN 1 ELSE 0 END) as design_count,           -- 디자인
            SUM(CASE WHEN ipr_code = '40' THEN 1 ELSE 0 END) as trademark_count         -- 상표
        FROM (
            SELECT pub_date, ipr_code FROM TB24_university_patent
            UNION ALL
            SELECT pub_date, ipr_code FROM TB24_university_design
            UNION ALL
            SELECT pub_date, ipr_code FROM TB24_university_trademark
        ) AS university_data
        WHERE pub_date >= '{one_day_ago}'  -- 하루 전 데이터만
        GROUP BY pub_date
        ORDER BY pub_date
    """
    university_date_data_day = fetch_data(university_date_query_day)

    # 대학교 등록 추세 라인 차트 생성 (한 달 간)
    university_line_chart_month = px.line(university_date_data, x='pub_date', y=['patent_count', 'design_count', 'trademark_count'], 
                                        title="대학교 등록 추세 (한 달 간)")

    university_line_chart_month.update_layout(xaxis_title="등록일", yaxis_title="등록 건수", legend_title="등록 종류", title_x=0.4)
    university_line_chart_month.update_traces(name='특허/실용신안 수', selector=dict(name='patent_count'))
    university_line_chart_month.update_traces(name='디자인 수', selector=dict(name='design_count'))
    university_line_chart_month.update_traces(name='상표 수', selector=dict(name='trademark_count'))

    # 하루 전 추세 라인 차트 생성 (1일 간)
    university_line_chart_day = px.line(university_date_data_day, x='pub_date', y=['patent_count', 'design_count', 'trademark_count'], 
                                        title="대학교 등록 추세 (1일 간)", line_shape='linear')
    
    university_line_chart_day.update_layout(xaxis_title="등록일", yaxis_title="등록 건수", legend_title="등록 종류", title_x=0.4)
    university_line_chart_day.update_traces(name='특허/실용신안 수', selector=dict(name='patent_count'))
    university_line_chart_day.update_traces(name='디자인 수', selector=dict(name='design_count'))
    university_line_chart_day.update_traces(name='상표 수', selector=dict(name='trademark_count'))

    st.plotly_chart(university_line_chart_day, use_container_width=True)
    st.plotly_chart(university_line_chart_month, use_container_width=True)
