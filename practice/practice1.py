# practice1.py
'''
    입력 함수 => input(출력할내용): 입력된값
        -> 기본적으로 입력된 값을 문자열 타입 리턴

        ex) name = input("이름 입력: ")
'''

# 1. 이름, 성별, 나이, 키 입력받아 출력
#  * 출력 형식 : 이름: xxx, 성별: xx, 나이: xx, 키: xx.xxcm
name = input("이름:")
sex = input("성별:")
age = input("나이:")
height = input("키:")
print(f"이름: {name}, 성별: {sex}, 나이: {age}, 키: {height}cm")
print()

# 2. 두 정수 입력받아 합, 차, 곱, 몫, 나머지 계산 후 출력
n1 = int(input("정수1 입력:"))
n2 = int(input("정수2 입력:"))

print("합:", n1 + n2)
print("차:", n1 - n2)
print("곱:", n1 * n2)
print("몫:", n1 // n2)
print("나머지:", n1 % n2)
print()

# 3. 영어 문자열 입력받아 앞 세 글자 출력
str = input("문자열 입력:")
print(str[0:3])
print()

# 4. 실수 2개 입력받아 합, 차, 곱, 나누기 출력
f1 = float(input("실수1 입력:"))
f2 = float(input("실수2 입력:"))

print("합:", f1 + f2)
print("차:", f1 - f2)
print("곱:", f1 * f2)
print("나누기:", f1 / f2)
print()

# 5. 두 수 입력받아 제곱과 제곱근 계산
i3 = int(input("정수1 입력:"))
i4 = int(input("정수2 입력:"))

print("정수1 제곱:", i3 ** 2)
print("정수1 제곱근:", i3 ** 0.5)
print("정수2 제곱:", i4 ** 2)
print("정수2 제곱근:", i4 ** 0.5)
print()

# 6. 문자열 입력받아 대문자/소문자/글자 수 출력
str2 = input("문자열 입력:")
print("대문자:", str2.upper())
print("소문자:", str2.lower())
print("글자 수:", len(str2))
print()

# 7. 좋아하는 음식 3개 입력받아 리스트처럼 저장 후 출력
food = []
food.append(input("좋아하는 음식1:"))
food.append(input("좋아하는 음식2:"))
food.append(input("좋아하는 음식3:"))

print("좋아하는 음식 리스트:", food)
print("첫 번째 음식:", food[0])
print("마지막 음식:", food[-1])
food.sort()
print("오름차순 정렬:", food)
food.reverse()
print("내림차순 정렬:", food)
print()

# 8. 세 개의 숫자 입력받아 합과 평균 계산 후 출력
n1 = int(input("정수1 입력:"))
n2 = int(input("정수2 입력:"))
n3 = int(input("정수3 입력:"))

print("합:", n1 + n2 + n3)
print("평균:", (n1 + n2 + n3) / 3)
print()

# 9. 문자열 입력받아 앞 3글자 + 뒤 2글자 합쳐서 출력
str = input("문자열 입력:")
print("앞 3글자 + 뒤 2글자:", str[0:3], str[-2:])
print()

# 10. 문자열 입력받아 대문자로 변환 후, 앞 5글자만 출력
str = input("문자열 입력:")
str2 = str.upper()
print("대문자 + 앞 5글자:", str2[0:5])