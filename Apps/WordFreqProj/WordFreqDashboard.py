import streamlit as st
import mylib.myTextMining as ta
import mylib.mySTVisualizer as sv
from konlpy.tag import Okt

# 사이드바 제목
st.sidebar.title("설정 메뉴")
# 데이터파일 업로드
uploaded_file = st.sidebar.file_uploader("데이터 파일을 선택하세요", type=['csv', 'xlsx'])
barhN = st.sidebar.slider("수평 막대 그래프 개수", min_value=10, max_value=50)
wcN = st.sidebar.slider("워드클라우드 단어 개수", min_value=10, max_value=100)
if uploaded_file is not None:
    # 1. 데이터 준비
    data, col = ta.load_data(uploaded_file)
    select_col = st.sidebar.selectbox("컬럼명", col)
    if st.sidebar.button("분석"):
        with st.spinner():
            corpus = ta.load_corpus(data, select_col)

        def review_data():
            # 2. 빈도수 만들기
            my_tags = ["Noun", "Verb", "Adjective"]
            my_stopwords = ["내", "내내", "티", "나", "들인건", "할수밖에", "없다", "보는", "정말", "하는", "보고", "입니다", "그냥", "정도", "해서", "있는", "봤는데", "것", "이", "더", "잘", "점", "좀", "그", "수", "할", ""]
            return ta.count_word_freq(corpus, Okt().pos, my_tags, my_stopwords)
        st.session_state["counter"] = review_data()
        st.success("분석 완료!")

    if "counter" in st.session_state:
        st.subheader("단어 빈도수 분석 결과")
        # 3. 수평 막대 그래프
        sv.visualize_barh_graph(st.session_state["counter"], barhN)    #num_word 추가 word개수 조절
        # 4. 워드클라우드
        sv.visualize_wordcloud(st.session_state["counter"], wcN)     #num_word 추가
    else:
        st.info("분석 시작 버튼을 눌러주세요.")
else:
    st.info("파일을 업로드해 주세요.")