#핸드폰 요금
#통화 시간 목록이 주어졌을 때, 
# 청구 방식이 다른 두 가지 요금제 중 더 저렴한 요금제를 구하는 문제.

def Ycost(times):
    total_cost = 0
    for time in times:
        total_cost += (time // 30 + 1) * 10
    return total_cost

def Mcost(times):
    total_cost = 0
    for time in times:
        total_cost += (time // 60 + 1) * 15
    return total_cost

def determine(times):
    ycost = Ycost(times)
    mcost = Mcost(times)
    
    if ycost < mcost:
        return f"Y {ycost}"
    elif mcost < ycost:
        return f"M {mcost}"
    else:
        return f"Y M {ycost}"

N = int(input())
times = list(map(int, input().split()))

print(determine(times))
