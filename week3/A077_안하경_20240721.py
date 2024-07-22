#점수 계산
#참가자의 8개 문제 점수가 주어졌을 때, 총 점수를 구하는 프로그램

scores = [int(input().strip()) for _ in range(8)]
indexed_scores = [(score, index + 1) for index, score in enumerate(scores)]
# 내림차순 정렬
indexed_scores.sort(reverse=True, key=lambda x: x[0])
# 상위 5개 점수
top_five_scores = indexed_scores[:5]
total_score = sum(score for score, index in top_five_scores)
# 포함된 문제 번호 정렬
problem_indices = sorted(index for score, index in top_five_scores)

print(total_score)
print(" ".join(map(str, problem_indices)))
