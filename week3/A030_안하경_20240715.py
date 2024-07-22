import numpy as np

def solution(N, mood, matrix):
    state = np.array([1, 0] if mood == 0 else [0, 1])
    for _ in range(N):
        state = np.dot(state, matrix)
        
    goodDay = round(state[0] * 1000)
    badDay = round(state[1] * 1000)
    
    return goodDay, badDay

# 입력 받기
N, mood = map(int, input().strip().split())
p_gg, p_gb, p_bg, p_bb = map(float, input().strip().split())

transition_matrix = np.array([[p_gg, p_bg], [p_gb, p_bb]])

good_day_prob, bad_day_prob = solution(N, mood, transition_matrix)
print(good_day_prob)
print(bad_day_prob)
