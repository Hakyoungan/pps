#다이얼
#알파벳을 입력 받고, 그 알파벳으로 전화를 걸 때 걸리는 최소 시간을 구하는 문제. 전화를 걸 때 걸리는 시간이 각 알파벳 별로 다르다. 
def solution(word):
    dialMapping = {
        'A': 2, 'B': 2, 'C': 2,
        'D': 3, 'E': 3, 'F': 3,
        'G': 4, 'H': 4, 'I': 4,
        'J': 5, 'K': 5, 'L': 5,
        'M': 6, 'N': 6, 'O': 6,
        'P': 7, 'Q': 7, 'R': 7, 'S': 7,
        'T': 8, 'U': 8, 'V': 8,
        'W': 9, 'X': 9, 'Y': 9, 'Z': 9
    }
    
    total_time = 0
    for char in word:
        total_time += dialMapping[char] + 1
    
    return total_time

word = input().strip()
print(solution(word))
