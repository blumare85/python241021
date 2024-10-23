import sqlite3
import random

class FoodBeverageManager:
    def __init__(self, db_name='food_beverage.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.conn.commit()

    def insert_product(self, name, price):
        self.cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))
        self.conn.commit()

    def update_product(self, product_id, name=None, price=None):
        if name and price:
            self.cursor.execute('UPDATE products SET name = ?, price = ? WHERE id = ?', (name, price, product_id))
        elif name:
            self.cursor.execute('UPDATE products SET name = ? WHERE id = ?', (name, product_id))
        elif price:
            self.cursor.execute('UPDATE products SET price = ? WHERE id = ?', (price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        self.cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
        self.conn.commit()

    def select_product(self, product_id=None):
        if product_id:
            self.cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
            return self.cursor.fetchone()
        else:
            self.cursor.execute('SELECT * FROM products')
            return self.cursor.fetchall()

    def generate_sample_data(self):
        food_items = ['피자', '햄버거', '파스타', '샐러드', '스테이크', '초밥', '라면', '김치찌개', '비빔밥', '치킨']
        beverage_items = ['콜라', '사이다', '주스', '커피', '차', '맥주', '와인', '소주', '물', '에이드']

        for _ in range(100):
            name = random.choice(food_items + beverage_items)
            price = round(random.uniform(1000, 50000), -2)  # 1,000원에서 50,000원 사이의 100원 단위 가격
            self.insert_product(name, price)

    def close(self):
        self.conn.close()

# 사용 예시
if __name__ == '__main__':
    manager = FoodBeverageManager()
    
    # 샘플 데이터 생성
    manager.generate_sample_data()
    
    # 전체 제품 조회
    all_products = manager.select_product()
    print(f"총 {len(all_products)}개의 제품이 있습니다.")
    
    # 첫 번째 제품 조회
    first_product = manager.select_product(1)
    print(f"첫 번째 제품: {first_product}")
    
    # 제품 업데이트
    manager.update_product(1, name="스페셜 피자", price=25000)
    updated_product = manager.select_product(1)
    print(f"업데이트된 제품: {updated_product}")
    
    # 제품 삭제
    manager.delete_product(100)
    
    # 데이터베이스 연결 종료
    manager.close()