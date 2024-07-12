#나누어 떨어지는 숫자 배열
def divide(arr, divisor):
    newarr=[num for num in arr if num%divisor==0]

    if not newarr:
        return[-1]
    
    return sorted(newarr)


print(divide([5, 9, 7, 10], 5))  #return [5,10]
print(divide([2, 36, 1, 3], 1))  #return [1,2,3,36]
print(divide([3, 2, 6], 10))   #return [-1]