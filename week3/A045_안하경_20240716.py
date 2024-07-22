#단어 공부
#알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성한다.
def solution(word):
    #문자 대문자로 변환
    word = word.upper()  
    frequency = {} 

    for char in word:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    # 가장 많이 사용된 알파벳 찾기
    max_freq = max(frequency.values())
    most_frequent = [char for char, freq in frequency.items() if freq == max_freq]

    # 가장 많이 사용된 알파벳이 여러 개인지 확인
    if len(most_frequent) > 1:
        return "?"
    else:
        return most_frequent[0]

word = input().strip()
print(solution(word))
