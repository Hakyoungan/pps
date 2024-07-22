#최소공배수
#두 수의 최소공배수를 구하는 문제
import math

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

def main():
    T = int(input())
    results = []
    for _ in range(T):
        A, B = map(int, input().split())
        results.append(lcm(A, B))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
