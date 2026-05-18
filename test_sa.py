from sentiment_analyzer import SentimentAnalyzer, korean_tokenizer

reviews = [
    '영화가 너무 재미있다',
    '영화가 너무 재미없다',
    '개꿀잼',
    '대유잼',
    '노잼',
    '영화 보다가 졸았음'
]

vectorizer_file = './model/sa_movie_vectorizer.pkl'
model_file = './model/sa_movie_model.pkl'

sa = SentimentAnalyzer(vectorizer_file, model_file)
for review in reviews:
    print(f'{review} -> {sa.analyze_sentiment(review)}')