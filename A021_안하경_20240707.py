#플러그
#하나의 플러그가 있고, N개의 멀티탭이 있다. 
# 각 멀티탭은 몇 개의 플러그로 이루어져 있다고 한다.
# 최대 몇 대의 컴퓨터를 전원에 연결할 수 있는지 출력하는 문제

def maxComputers(n, plugs):
    # 모든 멀티탭의 플러그 수 합산
    total = sum(plugs)
    
    # 총 플러그 수에서 (멀티탭 수 - 1) 을 빼줌
    max_computers = total - (n - 1)
    
    return max_computers

n = int(input())
plugs = [int(input()) for _ in range(n)]

print(maxComputers(n, plugs))
