# 4_inheritance.py

# 상속: 부모 클래스의 속성, 메소드들을 새로 정의하지 않고 사용할 수 있는 기술

# Animal 클래스 정의
class Animal:
    def eat(self):
        print("간식 우걱우걱")

    def speak(self):
        print("웁니다")

# Dog 클래스 정의
# Class Dog:
class Dog(Animal):
    '''
    def speak(self):
        print("댕댕~!")

    def eat(self):
        print("간식 버억")
    '''
    def speak(self):
        print("댕! 댕~!!")

    def play_ball(self):
        print("공놀이 ㄱㄱ")

# Dog 클래스 생성
d = Dog()
d.play_ball()
d.eat()
d.speak()