#Rotate String
#두 개의 문자열 s와 목표가 주어졌을 때 s에서 몇 번의 이동 후에 s가 목표가 될 수 있는 경우에만 true를 반환하는 문제
def goal(s, goal):
    if len(s) != len(goal):
        return False
    return goal in (s + s)

print(goal("abcde", "cdeab"))  
print(goal("abcde", "abced"))  
