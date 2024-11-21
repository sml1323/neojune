# pip install Flask Flask-SQLAlchemy pymysql
# Running on http://127.0.0.1:5000

# 복잡한 통계 쿼리는 피할 것



import json
from flask import Flask, render_template, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from datetime import datetime


# Flask 애플리케이션 객체 생성
app = Flask(__name__)

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://kipris:kipris1004@kt2.elementsoft.biz:13306/kipris?charset=utf8mb4'  # 실제 접속 정보 입력
    SQLALCHEMY_TRACK_MODIFICATIONS = False
app.config.from_object(Config)
db = SQLAlchemy(app)

# 기본 경로("/")에 대한 라우트 설정
@app.route("/")
def mainPage():
    return render_template("index.html")


@app.route("/company/<company_id>")
def companyPage(company_id):

    return render_template("company.html")


@app.route('/api/company/<int:company_id>', methods=['GET'])
def get_company_details(company_id):
    # 회사 상세 정보 쿼리
    sql = text("""
        SELECT 
            comp.company_seq as company_seq,
            comp.biz_no as biz_no,
            comp.corp_no as corp_no,
            comp.biz_type as biz_type,
            comp.company_name as company_name,
            -- 특허 통계
            (SELECT COUNT(*) FROM tb24_company_patent cpr WHERE cpr.applicant_id = applicant.applicant_id) AS cnt_patent,
            -- 상표 통계 (등록 날짜 대신 pub_date 사용)
            (SELECT COUNT(*) FROM tb24_company_trademark trademark WHERE applicant.applicant_id = trademark.applicant_id) AS cnt_trademark,
            -- 디자인 통계
            (SELECT COUNT(*) FROM tb24_company_design design WHERE applicant.applicant_id = design.applicant_id) AS cnt_design,
            -- 등록된 특허
            (SELECT COUNT(*) FROM tb24_company_patent cpr WHERE cpr.applicant_id = applicant.applicant_id AND cpr.reg_date IS NOT NULL) AS registered_patents,
            -- 공개된 특허
            (SELECT COUNT(*) FROM tb24_company_patent cpr WHERE cpr.applicant_id = applicant.applicant_id AND cpr.pub_date IS NOT NULL) AS published_patents,
            -- 등록된 상표 (등록 날짜 대신 pub_date 사용)
            (SELECT COUNT(*) FROM tb24_company_trademark trademark WHERE applicant.applicant_id = trademark.applicant_id AND trademark.pub_date IS NOT NULL) AS registered_trademarks,
            -- 공개된 상표
            (SELECT COUNT(*) FROM tb24_company_trademark trademark WHERE applicant.applicant_id = trademark.applicant_id AND trademark.pub_date IS NOT NULL) AS published_trademarks,
            -- 등록된 디자인
            (SELECT COUNT(*) FROM tb24_company_design design WHERE applicant.applicant_id = design.applicant_id AND design.reg_date IS NOT NULL) AS registered_designs,
            -- 공개된 디자인
            (SELECT COUNT(*) FROM tb24_company_design design WHERE applicant.applicant_id = design.applicant_id AND design.pub_date IS NOT NULL) AS published_designs
        FROM 
            tb24_100 AS comp
        JOIN 
            tb24_200 AS applicant
            ON comp.company_seq = applicant.app_seq
        WHERE comp.company_seq = :company_id
    """)

    result = db.session.execute(sql, {'company_id': company_id})

    company = result.fetchone()

    if company:
        company_data = {
            "company_seq": company.company_seq,
            "biz_no": company.biz_no,
            "corp_no": company.corp_no,
            "biz_type": company.biz_type,
            "company_name": company.company_name,
            "cnt_patent": company.cnt_patent,
            "cnt_trademark": company.cnt_trademark,
            "cnt_design": company.cnt_design,
            "registered_patents": company.registered_patents,
            "published_patents": company.published_patents,
            "registered_trademarks": company.registered_trademarks,
            "published_trademarks": company.published_trademarks,
            "registered_designs": company.registered_designs,
            "published_designs": company.published_designs
        }
        return jsonify({"company": company_data}), 200
    else:
        return jsonify({"message": "Company not found"}), 404
    

@app.route('/api/company/top10', methods=['GET'])
def get_top10_companies():
    sql = text("""
    SELECT t1.* 
    FROM (
        SELECT 
            comp.company_seq as company_seq,
            comp.biz_no as biz_no,
            comp.corp_no as corp_no,
            comp.biz_type as biz_type,
            comp.company_name as company_name,
            (SELECT COUNT(*) 
             FROM tb24_company_patent cpr 
             WHERE cpr.applicant_id = applicant.applicant_id) AS cnt_patent,
            (SELECT COUNT(*) 
             FROM tb24_company_trademark trademark 
             WHERE applicant.applicant_id = trademark.applicant_id) AS cnt_trademark,
            (SELECT COUNT(*) 
             FROM tb24_company_design design 
             WHERE applicant.applicant_id = design.applicant_id) AS cnt_design
        FROM 
            tb24_100 AS comp
        JOIN 
            tb24_200 AS applicant
            ON comp.company_seq = applicant.app_seq
    ) t1
    ORDER BY t1.cnt_patent + t1.cnt_trademark + t1.cnt_design DESC
    LIMIT 10;
    """)
    
    result = db.session.execute(sql)
    
    # 상위 10개 회사에 대한 통계 데이터
    top_companies_data = [
        {
            "company_seq": row[0],
            "biz_no": row[1],
            "corp_no": row[2],
            "biz_type": row[3],
            "company_name": row[4],
            "cnt_patent": row[5],
            "cnt_trademark": row[6],
            "cnt_design": row[7],
        }
        for row in result
    ]

    return jsonify({"top_companies": top_companies_data})

# 연도별 통계 API
@app.route('/api/statistics', methods=['GET'])
def get_patent_statistics():
    sql = text("""
        SELECT YEAR(tcd.reg_date) AS year, COUNT(*) AS count
        FROM tb24_company_patent tcd
        WHERE tcd.reg_date IS NOT NULL
        GROUP BY year
        HAVING year > 2010
        ORDER BY year;
    """)
    result = db.session.execute(sql)
    patent_data = [{"year": row.year, "count": row.count} for row in result]

    sql = text("""
        SELECT YEAR(tcd.pub_date) AS year, COUNT(*) AS count
        FROM tb24_company_trademark tcd
        WHERE tcd.pub_date IS NOT NULL
        AND tcd.legal_status_desc = '등록'
        GROUP BY year
        HAVING year > 2010
        ORDER BY year;
    """)
    result = db.session.execute(sql)
    trademark_data = [{"year": row.year, "count": row.count} for row in result]

    sql = text("""
        SELECT YEAR(tcd.reg_date) AS year, COUNT(*) AS count
        FROM tb24_company_design tcd
        WHERE tcd.reg_date IS NOT NULL
        GROUP BY year
        HAVING year > 2010
        ORDER BY year;
    """)
    result = db.session.execute(sql)
    design_data = [{"year": row.year, "count": row.count} for row in result]

    return jsonify({
        "patent_statistics": patent_data,
        "trademark_statistics": trademark_data,
        "design_statistics": design_data,
    })

@app.route('/api/statistics/count', methods=['GET'])
def get_total_counts():
    # 디자인 개수
    design_count_query = text("SELECT COUNT(*) AS count FROM tb24_company_design tcd;")
    design_count_result = db.session.execute(design_count_query).scalar()
    
    # 특허 개수
    patent_count_query = text("SELECT COUNT(*) AS count FROM tb24_company_patent tcd;")
    patent_count_result = db.session.execute(patent_count_query).scalar()
    
    # 상표 개수
    trademark_count_query = text("SELECT COUNT(*) AS count FROM tb24_company_trademark tcd;")
    trademark_count_result = db.session.execute(trademark_count_query).scalar()

    # 결과를 JSON 형식으로 반환
    return jsonify({
        "design_count": design_count_result,
        "patent_count": patent_count_result,
        "trademark_count": trademark_count_result
    })

# 애플리케이션 실행
if __name__ == "__main__":
    app.run(debug=True)