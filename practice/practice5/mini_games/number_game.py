# 숫자 맞추기 게임

import random


def play_number_game():
    
    while True:
        rand_num = random.randint(1, 10)
        print(f"답: {rand_num}")
        
        num = int(input("1에서 10 사이의 숫자를 입력하세요(종료는 0 입력): "))

        if num == 0:
            print("게임을 종료합니당")
            return
        
        if num > 10 or num < 0:
            print("범위 안의 숫자를 입력하세요")
            continue
        
        if rand_num is num:
            print("정답!")
        else:
            print(f"틀렸습니다. 정답은 {rand_num}였습니다.")
