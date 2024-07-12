#Single Number
#비어 있지 않은 정수 배열이 주어지면 모든 요소는 하나를 제외하고 두번 나타난다. 그 하나를 찾기.

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

print(singleNumber([2, 2, 1]))  
print(singleNumber([4, 1, 2, 1, 2]))
print(singleNumber([1]))  
print(singleNumber([1, 1, 2, 3, 3, 2, 5])) 
