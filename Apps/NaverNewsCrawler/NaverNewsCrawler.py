import os
import sys
import urllib.request
import json
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

def crawl_naver_news(url, start=0, display=10):
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    url += f'&start={start}&display={display}'
    
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read()
        # json_str = response_body.decode('utf-8')
        # py_data = json.load(json_str)
        # news_data = py_data['item']
        news_data = json.loads(response_body.decode('utf-8'))['items']
        # print(news_data)
        return news_data, None
    else:
        # print("Error Code:" + rescode)
        return None, rescode

def crawl_naver_news_all(keyword):
    encText = urllib.parse.quote(keyword)
    start = 1
    display = 10
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
    corpus = []
    while start <= 10:
        crawled_news, status = crawl_naver_news(url, start, display)
        if crawled_news:
            corpus += crawled_news
            start += display
        else:
            print("Error Code:" + status)
            break

    return corpus

def save_corpus(corpus, filename):
    print(1)
    print(corpus)
    news_list = []
    for item in corpus:
        print(2)
        print(item['title'])
        print(item['link'])
        print(item['description'])
        print(item['bloggername'])
        print(item['bloggerlink'])
        print(item['postdate'])
        # HTML 태그 제거 (<b> 등 제거)
        title = item['title'].replace("<b>", "").replace("</b>", "").replace("&quot;", "")
        description = item['description'].replace("<b>", "").replace("</b>", "").replace("&quot;", "")
        
        news_list.append({
            'title': title,
            'link': item['link'],
            'description': description,
            'bloggername': item['bloggername'],
            'bloggerlink': item['bloggerlink'],
            'postdate': item['postdate']
        })
    print(3)
    print(news_list)
    # 4. CSV 파일로 저장
    df = pd.DataFrame(news_list)
    print(df)
    df.to_csv(f"./result/{filename}.csv", index=False, encoding="utf-8-sig")
    print("CSV 파일 저장 완료!")