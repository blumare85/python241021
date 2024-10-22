#부모 클래스 정의
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

#자식 클래스 정의
class Student(Person):
    #덮어쓰기(재정의, override)
    def __init__(self, name, phoneNumber, subject, studentID):
        #명시적으로 부모 초기화 메서드 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #덮어쓰기
    def printInfo(self):
        print("Info(이름:{0}, 전화번호: {1})".format(self.name, self.phoneNumber))
        print("Info(학과:{0}, 학번: {1})".format(self.subject, self.studentID))

#인스턴스(특정 학생)
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "왜적토벌학과", "24000")
print(p.__dict__)
print(s.__dict__)

#메서드(부모로부터 상속받은 팔, 다리)
p.printInfo()
s.printInfo()


print("---ChatGPT Version---")

# Person 클래스
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")

# Manager 클래스 (Person을 상속)
class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title
    
    def printInfo(self):
        super().printInfo()
        print(f"Title: {self.title}")

# Employee 클래스 (Person을 상속)
class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill
    
    def printInfo(self):
        super().printInfo()
        print(f"Skill: {self.skill}")

# 테스트 코드
def test_classes():
    # 1. Person 객체 생성 및 정보 출력
    p1 = Person(1, "Alice")
    p1.printInfo()
    print()

    # 2. Person 객체 생성 및 정보 출력
    p2 = Person(2, "Bob")
    p2.printInfo()
    print()

    # 3. Manager 객체 생성 및 정보 출력
    m1 = Manager(3, "Charlie", "Project Manager")
    m1.printInfo()
    print()

    # 4. Manager 객체 생성 및 정보 출력
    m2 = Manager(4, "David", "HR Manager")
    m2.printInfo()
    print()

    # 5. Employee 객체 생성 및 정보 출력
    e1 = Employee(5, "Eve", "Python Developer")
    e1.printInfo()
    print()

    # 6. Employee 객체 생성 및 정보 출력
    e2 = Employee(6, "Frank", "Data Analyst")
    e2.printInfo()
    print()

    # 7. Manager 객체를 Person 변수에 저장 후 출력
    p3 = Manager(7, "Grace", "Sales Manager")
    p3.printInfo()
    print()

    # 8. Employee 객체를 Person 변수에 저장 후 출력
    p4 = Employee(8, "Hank", "DevOps Engineer")
    p4.printInfo()
    print()

    # 9. 동일한 이름을 가진 두 객체 비교
    p5 = Person(9, "Ivy")
    p6 = Person(9, "Ivy")
    print(f"p5과 p6이 동일 객체인가? {'Yes' if p5 == p6 else 'No'}")
    print()

    # 10. Manager와 Employee 객체의 다형성 테스트
    people = [Person(10, "John"), Manager(11, "Kim", "CTO"), Employee(12, "Lee", "Backend Developer")]
    for person in people:
        person.printInfo()
        print()

# 테스트 실행
test_classes()
