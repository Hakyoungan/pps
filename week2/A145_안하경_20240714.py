#부족한 금액 계산하기
#놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요. 단, 금액이 부족하지 않으면 0을 return 하세요.
def solution(price, money, count):
    # 총 금액 계산
    total_cost = (count * (price + price * count)) // 2
    
    # 모자라는 금액 계산
    shortage = total_cost - money
    
    return max(0, shortage)

price = 3
money = 20
count = 4
print(solution(price, money, count))
