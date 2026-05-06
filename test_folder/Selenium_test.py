from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 드라이버 설정
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 1. 해당 게시판 페이지로 이동
driver.get("https://www.kopo.ac.kr/seongnam/board.do?menu=13152")
time.sleep(2) # 페이지 로딩 대기

# # 2. 첫 번째 게시물의 제목 요소 찾기
# first_post = driver.find_element(By.CSS_SELECTOR, "td.b_subject a")

# # 3. .text와 .get_attribute() 비교해보기
# title_text = first_post.text  # 눈에 보이는 제목 글자
# post_url = first_post.get_attribute("href")  # 숨겨진 연결 주소

# print(f"제목: {title_text}")
# print(f"링크: {post_url}")

# try:
#     # 첨부파일 아이콘 이미지 요소 찾기
#     file_icon = driver.find_element(By.CSS_SELECTOR, "img[src*='file']")
    
#     # 이미지의 alt 속성(대체 텍스트) 가져오기
#     file_desc = file_icon.get_attribute("alt")
#     print(f"첨부파일 아이콘 설명: {file_desc}")
# except:
#     print("첨부파일이 있는 게시물이 현재 페이지에 없습니다.")

# # 1. 모든 제목 요소를 '그물'로 건져 올립니다.
# title_list = driver.find_elements(By.CSS_SELECTOR, "td.b_subject a")

# # 2. 리스트 형태이므로 for문을 사용해 하나씩 꺼냅니다.
# print(f"총 {len(title_list)}개의 게시물을 찾았습니다.")
# print("-" * 30)

# for title in title_list:
#     # 각 요소(title)에서 텍스트와 링크를 추출합니다.
#     name = title.text
#     link = title.get_attribute("href")
    
#     print(f"제목: {name}")
#     print(f"링크: {link}")
#     print("-" * 10)

# 모든 행(Row) 가져오기 (헤더 제외하고 본문 tr들만)
rows = driver.find_elements(By.CSS_SELECTOR, "tbody tr")

for row in rows:
    # 각 행 안에 있는 칸(td)들을 다시 찾습니다.
    # row.find_elements (driver가 아니라 row에서 찾음!)
    cols = row.find_elements(By.TAG_NAME, "td")
    if len(cols) > 1: # 데이터가 있는 행인지 확인
        subject = cols[1].text  # 제목 (성남폴리텍 게시판 기준 3번째 칸)
        date = cols[3].text     # 작성일 (성남폴리텍 게시판 기준 6번째 칸)
        
        print(f"{subject} | {date}")

driver.quit()