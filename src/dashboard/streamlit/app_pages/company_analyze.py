import streamlit as st


def display_company_analyze():
    st.subheader("분석")
    
    # Iframe을 통해 다른 웹페이지 삽입 (세로 100% 설정)
    iframe_code = """
    <style>
        body {{
            width: 100%;
            height: 100%;
            background-color: #333 !important;
        }}
        
        .iframe-container {{
            position: relative;
            width: 100%;
            height: 100vh;
            background-color: #333 !important;
            padding: 10px;
        }}
    </style>
    <div class="iframe-container">
        <iframe src="http://localhost:5000/" width="100%" height="1920px" frameborder="0"></iframe>
    </div>
    """
    st.markdown(iframe_code, unsafe_allow_html=True)