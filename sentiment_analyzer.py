# 한국어 토크나이저 정의
from konlpy.tag import Okt
def korean_tokenizer(text):
    my_tags = ['Noun', 'Adjective', 'Verb']
    my_stopwords = []
    tokenizer = Okt().pos
    return [word for word,  tag in tokenizer(text) if tag in my_tags and word not in my_stopwords]

# 모델 로딩
import joblib
class SentimentAnalyzer:
    def __init__(self, vectorizer_file, model_file):
        self.__vectorizer = joblib.load(vectorizer_file)
        self.__sa_model = joblib.load(model_file)

    def analyze_sentiment(self, review):
        # 전처리 및 특징 벡터 추출
        review_fv = self.__vectorizer.transform([review])
        # print(review_fv)

        result = self.__sa_model.predict(review_fv)
        # print(result)

        show = '긍정' if result[0] >= 0.5 else '부정'
        return show

