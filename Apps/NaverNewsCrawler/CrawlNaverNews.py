import NaverNewsCrawler as nnc
import streamlit as st

st.title("Hello, Streamlit World")
st.sidebar.subheader("네이버 뉴스 크롤러")
keyword =st.sidebar.text_input("검색할 키워드")

if st.sidebar.button("검색"):
    if keyword:
        st.session_state["corpus"] = nnc.crawl_naver_news_all(keyword)
    else:
        st.warning("키워드가 없습니다.")
    st.session_state["corpus"]

csv_file_name = st.sidebar.text_input("저장할 파일 이름")
if st.sidebar.button("저장"):
    nnc.save_corpus(st.session_state["corpus"], csv_file_name)