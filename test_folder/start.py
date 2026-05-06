import streamlit as st
import time

@st.cache_data
def change_text():
    text = st.title("텍스트 변합니다.")
    time.sleep(3)
    text = text.info("3초 지났습니다.")

change_text()
"바꿔보자"