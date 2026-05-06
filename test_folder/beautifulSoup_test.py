import requests
from bs4 import BeautifulSoup

# 1. 대상 URL 설정 및 데이터 요청
url = "https://www.kopo.ac.kr/seongnam/board.do?menu=13152"
response = requests.get(url)

# 2. BeautifulSoup 객체 생성
soup = BeautifulSoup(response.content, "html.parser")

# # 문서의 title 태그 내용 가져오기
# print(soup.title.string)
# # 문서의 첫 번째 span 태그 가져오기
# print(soup.span.text)

# # 태그 하나만 찾기
# fBoard = soup.find('a', {"class":"nav-skip__item"})
# print(fBoard)
# # 태그 전부를 리스트로 가져오기
# fBoards = soup.find_all('a', {"class":"nav-skip__item"})
# print(fBoards)

# # class가 b_subject안의 span태그 안의 a태그 찾기
# tabledata = soup.select_one(".b_subject > span > a")
# print(tabledata.text)

# tdtext = soup.select(".b_subject > span > a")
# for tdt in tdtext:
#     print(tdt.text) # 태그 안의 속성이 아니라 메서드 사용
#     print(tdt["href"])  # 태그안의 속성은 []로 접근 가능

# 2. 게시물 목록(행) 가져오기
# 공지사항 테이블의 모든 행(tr)을 가져옵니다.
rows = soup.select('table.tbl_list > tbody > tr')

for row in rows:
    # 3. 기준점 잡기: 제목이 들어있는 td를 먼저 찾습니다.
    # 클래스명이 'left'인 td가 제목을 포함하고 있습니다.
    title_td = row.find('td', class_='b_subject')
    
    if title_td:
        # 제목 텍스트 추출
        title = title_td.get_text(strip=True)
        
        # 4. 관계 탐색 시작 (형제 노드 찾기)
        # 제목(td) 바로 다음에 오는 형제 td들을 모두 가져옵니다.
        # [작성자td, 등록일td, 조회수td] 순서로 리스트가 반환됩니다.
        siblings = title_td.find_next_siblings('td')
        
        if len(siblings) >= 2:
            author = siblings[0].get_text(strip=True) # 첫 번째 형제: 작성자
            date = siblings[1].get_text(strip=True)   # 두 번째 형제: 등록일
            
            print(f"제목: {title}")
            print(f"작성자: {author} | 등록일: {date}")
            print("-" * 50)