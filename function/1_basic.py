# 1_basic.py
import random

# 매개변수가 없고, 반환 값도 없는 함수
def f1():
    print("난 f1 함수임")
    print("전달받는 값도 없고, 돌려줄 값도 없슴")

# f1()

# 매개변수가 있고, 반환값이 없는 함수
def f2(message):
    print("난 f2 함수야")
    print("전달된 값을 가지고 어떠한 기능 수행 가능함")
    print(f"*** {message} ***")

# f2("안농")


# 매개변수가 없고, 반환 값이 있는 함수
def f3():
    print("아임 f3 함수")
    print("전달받은 값은 없고, 주기만 함!")
    return random.randint(1, 100)

# f3()
# result = f3()
# print("f3 함수가 준 값", result)

# 매개변수, 반환 값 모두 있는 함수
def add(a, b):
    # 함수 첫 줄에 도움말 표시
    '''
        전달받은 두 수의 합을 구하는 함수

        Args:
            a: 첫번째 정수
            b: 두번째 정수

        Returns:
            a + b: 두 수의 합
    '''
    print("나는 add 함수야")
    print("전달 받은 두 수를 합해서 돌려줌")
    return a + b

result2 = add(5, 10)
print("add 함수가 돌려준 값", result2)