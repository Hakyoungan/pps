#OX퀴즈
#OX퀴즈의 결과가 String으로 주어졌을 때, 점수를 구하는 프로그램을 작성한다.
def solution(quizNum):
    total = 0
    streak = 0

    for char in quizNum:
        if char == 'O':
            streak += 1
            total += streak
        else:
            streak = 0
    
    return total

N = int(input().strip())
for _ in range(N):
    quizNum = input().strip()
    print(solution(quizNum))
