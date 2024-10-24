'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic 
import sqlite3
import os.path

#DB파일이 없으면 만들고 있다면 접속한다. 
if os.path.exists("ProductList.db"):
    con = sqlite3.connect("ProductList.db")
    cur = con.cursor()
else: 
    con = sqlite3.connect("ProductList.db")
    cur = con.cursor()
    cur.execute(
        "create table Products (id integer primary key autoincrement, Name text, Price integer);")

#디자인 파일을 로딩
form_class = uic.loadUiType("Chap10_ProductList.ui")[0]

class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        #초기값 셋팅 
        self.id = 0 
        self.name = ""
        self.price = 0 

        #QTableWidget의 컬럼폭 셋팅하기 
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        #QTableWidget의 헤더 셋팅하기
        self.tableWidget.setHorizontalHeaderLabels(["제품ID","제품명", "가격"])
        #QTableWidget의 컬럼 정렬하기 
        #self.tableWidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignRight)
        #self.tableWidget.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
        #탭키로 네비게이션 금지 
        self.tableWidget.setTabKeyNavigation(False)
        #엔터키를 클릭하면 다음 컨트롤로 이동하는 경우 
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())
        #더블클릭 시그널 처리
        self.tableWidget.doubleClicked.connect(self.doubleClick)

    def addProduct(self):
        #입력 파라메터 처리 
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()
        cur.execute("insert into Products (Name, Price) values(?,?);", 
            (self.name, self.price))
        #리프레시
        self.getProduct() 
        #입력,수정,삭제 작업후에는 커밋을 한다. 
        con.commit() 

    def updateProduct(self):
        #업데이트 작업시 파라메터 처리 
        self.id  = self.prodID.text()
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()
        cur.execute("update Products set name=?, price=? where id=?;", 
            (self.name, self.price, self.id))
        #리프레시
        self.getProduct() 
        #입력,수정,삭제 작업후에는 커밋을 한다. 
        con.commit()  

    def removeProduct(self):
        #삭제 파라메터 처리 
        self.id  = self.prodID.text() 
        strSQL = "delete from Products where id=" + str(self.id)
        cur.execute(strSQL)
        #리프레시
        self.getProduct() 
        #입력,수정,삭제 작업후에는 커밋을 한다. 
        con.commit()  

    def getProduct(self):
        #검색 결과를 보여주기전에 기존 컨텐트를 삭제(헤더는 제외)
        self.tableWidget.clearContents()

        cur.execute("select * from Products;") 
        #행숫자 카운트 
        row = 0 
        for item in cur: 
            int_as_strID = "{:10}".format(item[0])
            int_as_strPrice = "{:10}".format(item[2])
            
            #각 열을 Item으로 생성해서 숫자를 오른쪽으로 정렬해서 출력한다. 
            itemID = QTableWidgetItem(int_as_strID) 
            itemID.setTextAlignment(Qt.AlignRight) 
            self.tableWidget.setItem(row, 0, itemID)
            
            #제품명은 그대로 출력한다. 
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))
            
            #각 열을 Item으로 생성해서 숫자를 오른쪽으로 정렬해서 출력한다. 
            itemPrice = QTableWidgetItem(int_as_strPrice) 
            itemPrice.setTextAlignment(Qt.AlignRight) 
            self.tableWidget.setItem(row, 2, itemPrice)
            
            row += 1
            print("row: ", row)  

    def doubleClick(self):
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()
'''

#gpt 버전
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QFont
from PyQt5 import uic 
import sqlite3
import os.path

# Database handler class for managing all database operations
class DatabaseHandler:
    def __init__(self):
        if os.path.exists("ProductList.db"):
            self.con = sqlite3.connect("ProductList.db")
            self.cur = self.con.cursor()
        else:
            self.con = sqlite3.connect("ProductList.db")
            self.cur = self.con.cursor()
            self.cur.execute(
                "create table Products (id integer primary key autoincrement, Name text, Price integer);")

    def add_product(self, name, price):
        self.cur.execute("insert into Products (Name, Price) values(?,?);", (name, price))
        self.con.commit()

    def update_product(self, product_id, name, price):
        self.cur.execute("update Products set name=?, price=? where id=?;", (name, price, product_id))
        self.con.commit()

    def remove_product(self, product_id):
        self.cur.execute("delete from Products where id=?;", (product_id,))
        self.con.commit()

    def fetch_products(self):
        self.cur.execute("select * from Products;")
        return self.cur.fetchall()

# UI class for managing the main window and interacting with the user
class DemoForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

        # Create an instance of the DatabaseHandler
        self.db_handler = DatabaseHandler()

        # Setup UI elements
        self.setup_ui_elements()

    def setupUi(self):
        self.setGeometry(100, 100, 553, 755)
        self.setWindowTitle("Product Manager")

        self.label = QLabel("제품ID:", self)
        self.label.setGeometry(40, 20, 101, 61)
        self.label.setFont(self.create_font())

        self.label_2 = QLabel("제품명:", self)
        self.label_2.setGeometry(40, 100, 101, 61)
        self.label_2.setFont(self.create_font())

        self.label_3 = QLabel("가   격:", self)
        self.label_3.setGeometry(40, 190, 101, 61)
        self.label_3.setFont(self.create_font())

        self.prodID = QLineEdit(self)
        self.prodID.setGeometry(140, 40, 201, 31)
        self.prodID.setFont(self.create_font())

        self.prodName = QLineEdit(self)
        self.prodName.setGeometry(140, 120, 201, 31)
        self.prodName.setFont(self.create_font())

        self.prodPrice = QLineEdit(self)
        self.prodPrice.setGeometry(140, 210, 201, 31)
        self.prodPrice.setFont(self.create_font())

        self.pushButton = QPushButton("입력", self)
        self.pushButton.setGeometry(380, 20, 131, 51)
        self.pushButton.setFont(self.create_font())
        self.pushButton.clicked.connect(self.add_product)

        self.pushButton_2 = QPushButton("수정", self)
        self.pushButton_2.setGeometry(380, 80, 131, 51)
        self.pushButton_2.setFont(self.create_font())
        self.pushButton_2.clicked.connect(self.update_product)

        self.pushButton_3 = QPushButton("삭제", self)
        self.pushButton_3.setGeometry(380, 140, 131, 51)
        self.pushButton_3.setFont(self.create_font())
        self.pushButton_3.clicked.connect(self.remove_product)

        self.pushButton_4 = QPushButton("검색", self)
        self.pushButton_4.setGeometry(380, 200, 131, 51)
        self.pushButton_4.setFont(self.create_font())
        self.pushButton_4.clicked.connect(self.get_products)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(40, 280, 471, 421)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(13)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.doubleClicked.connect(self.double_click)
    
    def create_font(self):
        font = QFont("맑은 고딕", 20)
        font.setBold(True)
        return font

    def setup_ui_elements(self):
        # Prevent navigation via Tab key
        self.tableWidget.setTabKeyNavigation(False)

        # Connect returnPressed signal to move focus
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())

    def add_product(self):
        name = self.prodName.text()
        price = self.prodPrice.text()
        self.db_handler.add_product(name, price)
        self.get_products()

    def update_product(self):
        product_id = self.prodID.text()
        name = self.prodName.text()
        price = self.prodPrice.text()
        self.db_handler.update_product(product_id, name, price)
        self.get_products()

    def remove_product(self):
        product_id = self.prodID.text()
        self.db_handler.remove_product(product_id)
        self.get_products()

    def get_products(self):
        self.tableWidget.clearContents()
        products = self.db_handler.fetch_products()
        row = 0
        for item in products:
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(item[0])))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(item[2])))
            row += 1

    def double_click(self):
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    sys.exit(app.exec_())
