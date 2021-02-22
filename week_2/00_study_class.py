class Person:
    def __init__(self, param_name):  # param_name: 생성자에서 데이터 받기
        print("hi", self)  # self 를 constructor 를 사용해서 주입받고 호출하는 것까지 해
        self.name = param_name  # self 는 자기 자신을 지칭, 내 안에다가 name 이라고 하는 녀석을 변수로 만들어서 거기에 param_name 을 저장해두겠다는 의미

    # 다른 함수 추가, Person 이라는 클래스의 name 을 출력하는 함수
    def talk(self):
        print("안녕하세요, 제 이름은", self.name, "입니다.")

# 생성자: 객체를 생성할 때 쓰는 함수
# 클래서 만들 때 constructor 를 설정하기 위해서는 __init__ 이라는 함수 만들어야!
# 인자에 자기 자신을 넘겨주는 게 self, 파이썬 클래스가 알아서 자기 자신을 넘겨준다.
# init 은 생성했을 때!, Person() 하면 이 Person 이 호출된 순간에 그 내부에 있는 함수가 불리게 되어서 실행된 것이라고 생각하면 됨.
# Person() 가 __init__() 함수와 똑같다~
person_1 = Person("유재석")  # hi <__main__.Person object at 0x7fced71cafd0>
print(person_1)  # <__main__.Person object at 0x7fced71cafd0>
print(person_1.name)  # 유재석
person_1.talk()

person_2 = Person("박명수")
print(person_2)
print(person_2.name)
person_2.talk()

# 클래스를 이용하면 유사한 행동 or 유사한 데이터를 쌓을 수 있게 구조를 쉽게 만들 수 있다. 