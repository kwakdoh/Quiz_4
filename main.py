# 유아로부터 구구단을 출력할 최대 단수를 입력받음
max_dan = int(input("몇 단까지 출력할까요?: "))

def biresult(dan, i):
    result = dan * i

 # 구구단 출력
    for dan in range(1, max_dan + 1):
        print(f"--------{dan} ---------단")
        for i in range(1, dan + 1):
            biresult = dan * i
            print(dan,"X", i,"=", dan*i)
        print()
    return result

biresult(max_dan, 1)
