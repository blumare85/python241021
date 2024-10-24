import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# URL 설정
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4'

# 요청 보내기
response = requests.get(url)

# 응답 상태 확인
if response.status_code == 200:
    # BeautifulSoup 객체 생성
    soup = BeautifulSoup(response.text, 'html.parser')

    # 신문기사 제목을 포함하는 HTML 태그 찾기
    titles = soup.find_all('a', class_='news_tit')

    # Excel 워크북 생성
    wb = Workbook()
    ws = wb.active
    ws.title = 'News Titles'

    # 엑셀 파일에 제목 저장 (첫 번째 행에 제목을 작성)
    ws.append(["No.", "Title"])

    # 제목을 엑셀 파일에 추가
    for idx, title in enumerate(titles, 1):
        ws.append([idx, title.get_text()])

    # 엑셀 파일 저장
    wb.save("results.xlsx")
    print("results.xlsx 파일이 생성되었습니다.")
else:
    print(f"Failed to retrieve data: {response.status_code}")
