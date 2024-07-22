#수 뒤집기
#원래의 수와 뒤집은 수를 더한 것이 팰린드롬인지 판별
#수 124를 뒤집으면 421이 되고 이 두 수를 합하면 545가 된다. 124와 같이 원래 수와 뒤집은 수를 합한 수가 좌우 대칭이 되는지 테스트 하는 프로그램을 작성하시오.

def isPalindrome(num):
    return str(num) == str(num)[::-1]

def reverseAndAdd(N):
    reversed_N = int(str(N)[::-1])
    return N + reversed_N

def tryout():
    T = int(input())
    results = []
    for _ in range(T):
        N = int(input())
        result = reverseAndAdd(N)
        if isPalindrome(result):
            results.append("YES")
        else:
            results.append("NO")
    
    for result in results:
        print(result)
tryout()
