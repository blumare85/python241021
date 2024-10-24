# DemoForm2.py
# DemoForm2.ui(화면단) + DemoForm2.py(로직단)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
#웹크롤링에 관련된 선언
from bs4 import BeautifulSoup

#웹서버에 요청
import requests


#미리 디자인한 문서를 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]

#DemoForm클래스 정의(QMainWindow)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #슬롯메서드 추가
    def firstClick(self):
        url = "https://www.daangn.com/fleamarket/"
        response = requests.get(url)

        #검색이 용이한 객체 생성
        soup = BeautifulSoup(response.text, "html.parser")

        #파일에 저장
        #f = open("daangn.txt", "wt", encoding="utf-8")
        f = open("daangn.txt", "a+", encoding="utf-8")
        posts = soup.find_all("div", attrs={"class":"card-desc"})
        for post in posts:
            titleElem = post.find("h2", attrs={"class":"card-title"})
            priceElem = post.find("div", attrs={"class":"card-price"})
            regionElem = post.find("div", attrs={"class":"card-region-name"})
            title = titleElem.text.replace("\n", "").strip()
            price = priceElem.text.replace("\n", "").strip()
            region = regionElem.text.replace("\n", "").strip()
            #내부에 문자열 출력:f-string
            print(f"{title}, {price}, {region}")
            f.write(f"{title}, {price}, {region}\n")

        f.close()
        self.label.setText("당근마켓 크롤링을 완료했습니다.")
    def secondClick(self):
        self.label.setText("두번째 클릭해부렀당께요.")
    def thirdClick(self):
        self.label.setText("세번째 클릭했지라.")

#진입점 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = DemoForm()
    myWindow.show()
    app.exec_()
