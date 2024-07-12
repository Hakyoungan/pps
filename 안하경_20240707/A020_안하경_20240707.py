#지능형 기차
#4개의 역에 대해 기차에서 내린 사람 수와 탄 사람 수가 주어졌을 때, 기차에 사람이 가장 많을 때의 사람 수를 계산하는 문제

def train():
    #4개의 각 역에서 내린 사람 수와 탐 사람 수 입력받기
    stations=[list(map(int, input().split())) for _ in range(4)]

    currentNum=0
    max=0

    for out, inc in stations:
        currentNum-=out
        currentNum+=inc
        if currentNum>max:
            max=currentNum

    print(max)

train()


