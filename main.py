# 유아로부터 구구단을 출력할 최대 단수를 입력받음
max_dan = int(input("몇 단까지 출력할까요?: "))

# 구구단 출력
for dan in range(1, max_dan + 1):
    print(f"--------{dan} ---------단")
    for i in range(1, dan + 1):
        result = dan * i
        print(f"{dan} x {i} = {result}")
    print()