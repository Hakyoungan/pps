#방번호
#방 번호 N을 만들기 위해 필요한 숫자 세트의 개수를 구하는 문제. 단, 6과 9는 뒤집어서 서로로 이용할 수 있다.

def setNum(num):
    #방번호를 문자열로 변환하여 각 숫자의 빈도를 계산
    count=[0]*10
    for digit in str(num):
        count[int(digit)]+=1

    #6과 9는 합쳐서 계산
    count[6]=(count[6]+count[9]+1)//2
    count[9]=0

    return max(count)

num=input().strip()

print(setNum(num))