import streamlit as st
import pandas as pd
import time

# Streamlit의 code 기본 구조
# Streamlit 코드와 python 코드가 특별한 구분자 또는 지시자 없이 혼합하여 사용함
st.title("Hello, Streamlit World")

name = "SJ"
st.title(f"Hello, {name}~~ Welcome to Streamlit World!!")

# Streamlit 기본 API 살펴보기
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B' : [10, 20, 30, 40]
})

# Write, Magic Command
st.write(df)
df

# Text 출력
@st.cache_data
def change_text():
    text = st.title("제일 큰 글자")
    time.sleep(0.5)
    text.header("title 보다 작은 글자")
    time.sleep(0.5)
    text.subheader("일반 글자보다 약간 큼")
    time.sleep(0.5)
    text.text("일반 텍스트")
change_text()

# 특정 상황에 사용하는 Text
st.success("성공")
st.warning("경고")
st.info("정보")
st.error("오류")

# Streamlit 기본 API 살펴보기
mn = ["신경망", "랜덤포레스트", "SVM"]
if st.button("button_name"):    # 버튼클릭 여부 True, False (옵션 확인해보기)
    st.success("clicked button")
ch = st.radio("머신러닝 방법", mn)  # 선택한 항목의 text를 반환 (옵션 확인해보기)
st.info(f"나의 선택 : {ch}")
st.checkbox("토큰화")   # check 여부 True, False
sel = st.selectbox("머신러닝 방법", mn) # 선택한 항목의 text반환 (옵션 확인해보기)
st.info(sel)
st.multiselect("머신러닝 방법", mn) # 선택한 항목을 list로 반환 (옵션 확인해보기)
num = st.slider("가중치")   #슬라이드바로 선택한 숫자 반환
st.info(f"가중치 : {num}")
st.text_input("텍스트를 입력 하세요")   #텍스트를 입력받는 창 생성 괄호는 label붙이기
st.number_input("숫자를 입력하세요")    #숫자를 입력받는 창 생성 입력값의 범위, 소수점 찍는 위치 정할 수 있음


with st.form('my_form'):
    st.subheader("사용자 입력 폼")
    name = st.text_input("이름")
    age = st.number_input("나이", step=1)
    agree = st.checkbox("약관에 동의합니다")
    submitted = st.form_submit_button('제출')
if submitted:
    st.text(f"이름 : {name} , 나이 : {age}")
    if agree:
        st.success("약관에 동의했습니다.")
    else:
        st.warning("약관에 동의하지 않았습니다.")

st.sidebar.subheader("설정")
st.sidebar.text_input("이름을 입력하세요")
st.sidebar.slider("나이", max_value=120)
st.sidebar.selectbox("좋아하는 색상을 선택하세요", ["빨강", "초록", "파랑"])

# matplotlib 사용
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt


font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

x = ['한다', '법률', '대통령', '국가', '국회', '의하여', '국민', '하여', '있다', '헌법']
y = [155, 127, 83, 73, 68, 66, 61, 61, 57, 53]

fig, ax = plt.subplots()
# 수평 막대그래프
ax.barh(x[::-1], y[::-1])

st.pyplot(fig)


# wordcloud 사용
from konlpy.corpus import kolaw
from wordcloud import WordCloud

input_filename = 'constitution.txt'
# 한글 폰트 path 지정
font_path = "c:/Windows/fonts/malgun.ttf"

fig1, ax1 = plt.subplots()
# WordCloud 객체 생성
const_wc = WordCloud(font_path = font_path,
                     width= 800,
                     height= 600,
                     background_color= "#FF69B4",
                     max_words= 50
                     )

const_wc = const_wc.generate(kolaw.open(input_filename).read())

ax1.imshow(const_wc)
ax1.axis(False)
st.pyplot(fig1)




import streamlit as st
import pandas as pd

df = pd.DataFrame({'id': [1, 2], 'value': [10, 20]})

st.write("### 데이터 확인", df) # st.write 사용
df # Magic 사용 (화면에 데이터프레임이 바로 나타남)






st.title("앱의 메인 제목")
st.header("섹션")
st.subheader("하위섹션")
st.markdown("텍스트 스타일링")
st.caption("출처나 주석을 위한 작은 폰트")



# st.map 예시
import pandas as pd
import numpy as np

# 'lat'과 'lon'이라는 컬럼명이 필수입니다.
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.56, 126.97],
    columns=['lat', 'lon'])

st.map(map_data)



# 슬라이더를 이용한 데이터 필터링 로직
# 사용자가 슬라이더를 움직이면 'selected_year' 변수가 즉시 업데이트되고 앱이 재실행됩니다.
selected_year = st.slider('연도 선택', 2015, 2023, 2020)
st.write(f"선택된 연도: {selected_year}년 데이터입니다.")

# 컬럼 배치 베스트 프랙티스
col1, col2 = st.columns([2, 1]) # 2:1 비율로 분할
with col1:
    st.header("메인 차트 영역")
    st.line_chart([1, 5, 200, 6])
with col2:
    st.header("상세 정보")
    st.write("차트에 대한 세부 설명입니다.")

