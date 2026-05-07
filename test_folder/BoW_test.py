from sklearn.feature_extraction.text import CountVectorizer

# 객체 생성
vectorizer = CountVectorizer(
    tokenizer ="",    # 토큰화 : 미지정 시 자체적으로 토큰화 수행 - 토큰화 성능을 높이고 싶을 때 tokenizer를 지정하여 객체 생성
    stop_words="",    # 불용어 제거 - defualt 자체 불용어 사전 이름 명시
    max_feature="",   # 최대 단어 수
    min_df="",        # 최소 빈도수
    max_df=""         # 최대 빈도수
)

# 특징 집합 구성
vectorizer.fit(corpus)
vectorizer.get_feature_names_out()

# 특징 벡터 추출
dtm = vectorizer.transform(list_of_text)
dtm.toarray()