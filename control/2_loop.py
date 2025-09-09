# 2_loop.py

# 반복문
'''
    * 기본 구조

        for 변수명 in 반복가능객체: 
            반복 내용
        # 가능한 객체: 리스트, 튜플 세트, 딕셔너리, 문자열

    * range 함수
        range(stop): 0 부터 stop - 1 까지 1씩 증가하는 숫자 생성(시퀸스)
        range(start, stop): stop 부터 stop - 1 까지 1씩 증가하는 숫자 생성(시퀸스)
        range(start, stop, step): stop 부터 stop - 1 까지 step씩 증가하는 숫자 생성(시퀸스)
'''
# * 1 ~ 10까지 출력
import random


for i in range(1, 11):
    print(i, end = " ")
print()

colors = ["red", "black", "white"]
for c in colors:
    print(c, end = " ")
print()

# while 문
'''
    * 기본 구조

        while 조건식:
            반복할 내용
'''
# while문을 사용하여 1 ~ 10 출력
n = 1
while n <= 10:
    print(n, end = " ")
    n += 1
print()

# while문을 사용하여 사용자 입력이 exit인 경우 종료
#                       그렇지 않으면 입력값 출력

while True:
    data = input("단어 입력하세요(exit 입력 시 종료): ")

    if data == 'exit':
        print("프로그램 종료")
        break
    
    print(f"입력된 값: {data}")

# * 업앤다운 게임
# 1 ~ 100 사이의 숫자 맞추기 게임
"""
    ex) 정답 = 55
        사용자: 20 Up!
        사용자: 60 Down!

        사용자: 55 정답!!
"""

print("*====== Up & Down ======*")
num = random.randint(1, 100)

#print(f"정답 = {num}")

while True:
    pick = (input("사용자: "))

    if not pick.isdigit():
        print("숫자만 ㄱㄱ")
        continue

    pick = int(pick)

    if pick == num:
        print(f"{num} 정답~")
        break
    elif pick < num:
        print("Up!")
    else:
        print("Down!")


rps = ["가위", "바위", "보"]
# (사용자값, 컴퓨터값)
win_case = [("가위", "보"), ("바위", "가위"), ("보", "바위")]
win_count = 0
n = 1


while n < 4:
    print(f"{n}회차")
    user = input("갈바 ㄱㄱ: ")

    if user in rps:
        com = random.choice(rps)

        print(f"나: {user} 컴터: {com}")

        if user == com:
            print("비김요")
        elif (user, com) in win_case:
            print("이김 ㅎ")
            win_count += 1
        else:
            print("짐 ㅠ")
    else:
        print("잘못 입력함 ㅠ")
        print()
        continue

    n += 1
    print()

print(f"{win_count}번 이김!")
