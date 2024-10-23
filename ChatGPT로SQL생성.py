import sqlite3
import random

# 클래스 정의
class ElectronicsDB:
    def __init__(self, db_name="electronics.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """전자제품 테이블 생성"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.conn.commit()

    def insert_product(self, name, price):
        """제품 데이터 삽입"""
        self.cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
        self.conn.commit()

    def update_product(self, product_id, name=None, price=None):
        """제품 데이터 수정"""
        if name and price:
            self.cursor.execute("UPDATE products SET name = ?, price = ? WHERE id = ?", (name, price, product_id))
        elif name:
            self.cursor.execute("UPDATE products SET name = ? WHERE id = ?", (name, product_id))
        elif price:
            self.cursor.execute("UPDATE products SET price = ? WHERE id = ?", (price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        """제품 데이터 삭제"""
        self.cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        self.conn.commit()

    def select_all_products(self):
        """모든 제품 데이터 조회"""
        self.cursor.execute("SELECT * FROM products")
        return self.cursor.fetchall()

    def select_product_by_id(self, product_id):
        """특정 제품 데이터 조회"""
        self.cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        return self.cursor.fetchone()

    def close(self):
        """연결 닫기"""
        self.conn.close()

# 샘플 데이터 100개 생성 및 삽입
def generate_sample_data(db):
    product_names = ['Smartphone', 'Laptop', 'Tablet', 'Smartwatch', 'Headphones', 'Camera', 'Television', 'Microwave', 'Refrigerator', 'Air Conditioner']
    
    for i in range(100):
        name = random.choice(product_names) + f" {i+1}"
        price = round(random.uniform(50.0, 2000.0), 2)
        db.insert_product(name, price)

# 메인 함수
if __name__ == "__main__":
    db = ElectronicsDB()

    # 샘플 데이터 생성
    generate_sample_data(db)

    # 삽입 후 데이터 조회
    products = db.select_all_products()
    for product in products:
        print(product)

    # 데이터 수정 예시
    db.update_product(1, name="Updated Smartphone", price=999.99)

    # 수정 후 특정 데이터 조회
    print("Updated Product:", db.select_product_by_id(1))

    # 데이터 삭제 예시
    db.delete_product(2)

    # 삭제 후 전체 데이터 조회
    print("Remaining Products:", db.select_all_products())

    # 연결 종료
    db.close()
