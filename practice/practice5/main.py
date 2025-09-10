
from mini_games import play_number_game, play_rps_game, play_dice_game

while True:
    print("*====== KH MINI GAME ======*")
    print("\t1. 숫자 맞추기")
    print("\t2. 가위바위보")
    print("\t3. 주사위 게임")
    print("\t0. 종료")

    print()

    menu = input("게임 선택: ")

    if menu == "1":
        # 숫자 맞추기 게임 실행
        play_number_game()
        pass
    elif menu == "2":
        # 가위바위보 게임 실행
        play_rps_game()
        pass
    elif menu == "3":
        # 주사위게임 실행
        play_dice_game()
        pass
    elif menu == "0":
        print("*======== GAME END ========*")
        break
    else:
        print("잘못 입력했습니다. 다시 입력해주세요.")