#농구 경기
#농구 선수를 선발할 수 있는 경우에는 가능한 성의 첫 글자를 사전순으로 공백없이 모두 출력하고 그렇지 않으면 PREDAJA를 출력하는 문제
def solution(players):
    first_letter_count = {}
    
    for player in players:
        first_letter = player[0]
        if first_letter in first_letter_count:
            first_letter_count[first_letter] += 1
        else:
            first_letter_count[first_letter] = 1
    
    starters = [letter for letter, count in first_letter_count.items() if count >= 5]
    
    if starters:
        return ''.join(sorted(starters))
    else:
        return "PREDAJA"

# 입력 받기
N = int(input().strip())
players = [input().strip() for _ in range(N)]

# 결과 출력
print(solution(players))

