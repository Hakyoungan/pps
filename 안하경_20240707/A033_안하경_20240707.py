#나는 요리사다
#총 다섯 개 줄에 각 참가자가 얻은 네 개의 평가 점수가 공백으로 구분되어 주어진다. 
#우승자의 번호와 그가 얻은 점수를 출력하는 문제

sheff = 5
scores = []

for _ in range(sheff):
    scores.append(sum(map(int, input().split())))

#최고 점수
max_score = max(scores)
#우승자
winner = scores.index(max_score) + 1

print(winner, max_score)
