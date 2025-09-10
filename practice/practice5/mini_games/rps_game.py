# 가위바위보 게임

import random


def play_rps_game():
    rps = ("가위", "바위", "보")
    win_case = [("가위", "보"), ("바위", "가위"), ("보", "바위")]
    
    
    while True:
        rand_rps = random.choice(rps)
        print(f"답: {rand_rps}")
        player_rps = input("가위 바위 보 뭘 낼래요??(종료는 0 입력): ")
        
        if player_rps == "0":
            print("게임을 종료합니당")
            return

        if rps.count(player_rps) == 0:
            print("가위바위보 중 하나를 내세요")
            continue
        
        if rand_rps == player_rps:
            print("비김!")
        elif (player_rps, rand_rps) in win_case:
            print("이김!")
        else:
            print("짐ㅠ")
