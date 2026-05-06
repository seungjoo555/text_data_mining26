import pandas as pd
from collections import Counter

def load_data(datafile):
    data_df = pd.read_csv(datafile)
    column = data_df.columns
    return data_df, column


# csv 파일에 분석 대상 텍스트를 추출하여 밚솬
# input : csv 파일, 분석 대상 컬럼명
# output : 텍스트의 리스트
def load_corpus(datafile, col_name):
    col_data = list(datafile[col_name])
    return col_data


def tokenize_korean_corpus(copus, tokenizer, my_tags, my_stopwords):
    tokens = []
    for i in range(len(copus)):
        tokens += [word for word, tag in tokenizer(copus[i]) if tag in my_tags and word not in my_stopwords]
    return tokens


# input : 텍스트의 리스트
# output : Counter 객체 (빈도수)
def count_word_freq(corpus, tokenizer, my_tags, my_stopwords):
    tokens = tokenize_korean_corpus(corpus, tokenizer, my_tags, my_stopwords)
    # 단어 빈도수 계산
    return Counter(tokens)