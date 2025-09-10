# 주사위 게임

import random

def play_dice_game():

    while True:

        num = int(input("시작은 1, 종료는 0: "))

        if num == 0:
            return
        elif num != 1:
            print("잘못 입력 하셨서용")
            continue

        player_dice = random.randint(1, 6)
        com_dice = random.randint(1, 6)

        print(f"플레이어: {player_dice} vs 컴퓨터: {com_dice}")

        if player_dice == com_dice:
            print("결과: 비김!")
        elif player_dice > com_dice:
            print("결과: 이김!")
        else:
            print("결과: 짐ㅠ")
