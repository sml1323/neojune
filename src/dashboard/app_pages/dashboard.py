import streamlit as st
import pandas as pd
import plotly.express as px
from db_connection import fetch_data

# 기업/대학별 데이터 시각화 및 요약
def display_dashboard_summary():
    st.subheader("산업재산권 데이터 요약")
    
    # 기업 요약 - 특허, 디자인, 상표
    company_query = """
        SELECT applicant, 
            SUM(CASE WHEN ipr_code IN ('10', '20') THEN 1 ELSE 0 END) as patent_count,  -- 특/실
            SUM(CASE WHEN ipr_code = '30' THEN 1 ELSE 0 END) as design_count,           -- 디자인
            SUM(CASE WHEN ipr_code = '40' THEN 1 ELSE 0 END) as trademark_count         -- 상표
        FROM (
            SELECT applicant, ipr_code FROM TB24_company_patent
            UNION ALL
            SELECT applicant, ipr_code FROM TB24_company_design
            UNION ALL
            SELECT applicant, ipr_code FROM TB24_company_trademark
        ) AS company_data
        GROUP BY applicant
        ORDER BY patent_count DESC
        LIMIT 10
    """
    company_data = fetch_data(company_query)
    # 총 기업 데이터 건수 계산 (전체 기업 데이터의 합)
    company_total_query = """
        SELECT 
            SUM(CASE WHEN ipr_code IN ('10', '20') THEN 1 ELSE 0 END) as patent_count,  -- 특/실
            SUM(CASE WHEN ipr_code = '30' THEN 1 ELSE 0 END) as design_count,           -- 디자인
            SUM(CASE WHEN ipr_code = '40' THEN 1 ELSE 0 END) as trademark_count         -- 상표
        FROM (
            SELECT ipr_code FROM TB24_company_patent
            UNION ALL
            SELECT ipr_code FROM TB24_company_design
            UNION ALL
            SELECT ipr_code FROM TB24_company_trademark
        ) AS company_data
    """
    company_total_data = fetch_data(company_total_query)
    company_totals = company_total_data.iloc[0].sum()  # 총합 계산

    # 대학 요약 - 특허, 디자인, 상표
    university_query = """
        SELECT applicant, 
            SUM(CASE WHEN ipr_code IN ('10', '20') THEN 1 ELSE 0 END) as patent_count,  -- 특/실
            SUM(CASE WHEN ipr_code = '30' THEN 1 ELSE 0 END) as design_count,           -- 디자인
            SUM(CASE WHEN ipr_code = '40' THEN 1 ELSE 0 END) as trademark_count         -- 상표
        FROM (
            SELECT applicant, ipr_code FROM TB24_university_patent
            UNION ALL
            SELECT applicant, ipr_code FROM TB24_university_design
            UNION ALL
            SELECT applicant, ipr_code FROM TB24_university_trademark
        ) AS university_data
        GROUP BY applicant
        ORDER BY patent_count DESC
        LIMIT 10
    """
    university_data = fetch_data(university_query)
    # 총 대학 데이터 건수 계산 (전체 대학 데이터의 합)
    university_total_query = """
        SELECT 
            SUM(CASE WHEN ipr_code IN ('10', '20') THEN 1 ELSE 0 END) as patent_count,  -- 특/실
            SUM(CASE WHEN ipr_code = '30' THEN 1 ELSE 0 END) as design_count,           -- 디자인
            SUM(CASE WHEN ipr_code = '40' THEN 1 ELSE 0 END) as trademark_count         -- 상표
        FROM (
            SELECT ipr_code FROM TB24_university_patent
            UNION ALL
            SELECT ipr_code FROM TB24_university_design
            UNION ALL
            SELECT ipr_code FROM TB24_university_trademark
        ) AS university_data
    """
    university_total_data = fetch_data(university_total_query)
    university_totals = university_total_data.iloc[0].sum()  # 총합 계산

    # 요약 카드 표시
    col1, col2 = st.columns(2)
    
    # metric 함수는 int, float, str, 또는 None만 허용 -> int()로 변환
    col1.metric("총 기업 데이터 건수", f"{int(company_totals):,} 건")
    col2.metric("총 대학 데이터 건수", f"{int(university_totals):,} 건")

    st.markdown("<br>", unsafe_allow_html=True) 

    # 기업 및 대학별 일일 업데이트 데이터
    st.subheader("🔍 **기업 및 대학별 일일 Update**")

    # 기업 일일 업데이트
    daily_company_query = """
        SELECT applicant, service_type, COUNT(*) as daily_count, legal_status_desc, update_date
        FROM daily_update_company
        WHERE update_date = CURDATE()
        GROUP BY applicant, service_type, legal_status_desc, update_date;  
    """
    daily_company_data = fetch_data(daily_company_query)
    if not daily_company_data.empty:
        st.subheader("기업 일일 등록 업데이트")
        st.dataframe(daily_company_data, use_container_width=True)

    # 대학 일일 업데이트
    daily_university_query = """
        SELECT applicant, service_type, COUNT(*) as daily_count, legal_status_desc, update_date
        FROM daily_update_university
        WHERE update_date = CURDATE()
        GROUP BY applicant, service_type, legal_status_desc, update_date;
    """
    daily_university_data = fetch_data(daily_university_query)
    if not daily_university_data.empty:
        st.subheader("대학 일일 등록 업데이트")
        st.dataframe(daily_university_data, use_container_width=True)

    # 기업별 일일 업데이트 데이터 표시
    st.markdown("📍 **기업별 Daily Update 산업재산권**")
    st.dataframe(daily_company_data.rename(columns={'applicant': '기업명', 'service_type': '등록 종류', 'legal_status_desc': '법적 상태', 'daily_count': '등록 건수', 'update_date': '변경일'}), use_container_width=True)

    # 대학별 일일 업데이트 데이터 표시
    st.markdown("📍 **대학별 Daily Update 산업재산권**")
    st.dataframe(daily_university_data.rename(columns={'applicant': '대학명', 'service_type': '등록 종류', 'legal_status_desc': '법적 상태', 'daily_count': '등록 건수', 'update_date': '변경일'}), use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True) 

    # 상위 기업/대학 건수 표
    st.markdown("✅ **등록 건수 상위 10개 기업**")
    company_data_reset = company_data.reset_index(drop=True)
    company_data_reset.index += 1  # 인덱스를 1부터 시작
    st.dataframe(company_data_reset.rename(columns={'applicant': '기업명', 'patent_count': '특허/실용신안 등록 건수', 
                                                    'design_count': '디자인 등록 건수', 'trademark_count': '상표 등록 건수'}), use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True) 

    st.markdown("✅ **등록 건수 상위 10개 대학교**")
    university_data_reset = university_data.reset_index(drop=True)
    university_data_reset.index += 1  # 인덱스를 1부터 시작
    st.dataframe(university_data_reset.rename(columns={'applicant': '대학명', 'patent_count': '특허/실용신안 등록 건수', 
                                                       'design_count': '디자인 등록 건수', 'trademark_count': '상표 등록 건수'}), use_container_width=True)
    st.markdown("<br>", unsafe_allow_html=True) 

    # 최근 7일간 등록 추세
    st.markdown("🔍 **최근 7일간 등록 추세**")
    date_query = """
        SELECT pub_date, 
            SUM(CASE WHEN ipr_code IN ('10', '20') THEN 1 ELSE 0 END) as patent_count,  -- 특/실
            SUM(CASE WHEN ipr_code = '30' THEN 1 ELSE 0 END) as design_count,           -- 디자인
            SUM(CASE WHEN ipr_code = '40' THEN 1 ELSE 0 END) as trademark_count         -- 상표
        FROM (
            SELECT pub_date, ipr_code FROM TB24_company_patent
            UNION ALL
            SELECT pub_date, ipr_code FROM TB24_company_design
            UNION ALL
            SELECT pub_date, ipr_code FROM TB24_company_trademark
        ) AS company_data
        WHERE pub_date >= DATE_SUB(CURDATE(), INTERVAL 7 DAY)
        GROUP BY pub_date
        ORDER BY pub_date
    """
    date_data = fetch_data(date_query)
    line_chart = px.line(date_data, x='pub_date', y=['patent_count', 'design_count', 'trademark_count'], 
                         title="최근 7일간 등록 추세")
    # x축과 y축의 레이블 변경
    line_chart.update_layout(
        xaxis_title="등록일", 
        yaxis_title="등록 건수", 
        legend_title="등록 종류", 
        title_x=0.5  # 제목 가운데 정렬
    )

    # 각 트레이스의 레이블 변경
    line_chart.update_traces(
        name='특허/실용신안 수',  # 첫 번째 트레이스 (특허/실용신안 수)
        selector=dict(name='patent_count')
    )

    line_chart.update_traces(
        name='디자인 수',  # 두 번째 트레이스 (디자인 수)
        selector=dict(name='design_count')
    )

    line_chart.update_traces(
        name='상표 수',  # 세 번째 트레이스 (상표 수)
        selector=dict(name='trademark_count')
    )

    st.plotly_chart(line_chart, use_container_width=True)
