#Move Zeroes
#정수 배열 nums가 주어지면 0이 아닌 요소의 상대적 순서를 유지하면서 모든 0을 끝으로 이동하는 문제
def moveZeroes(nums):
    j = 0  
    for i in range(len(nums)):
        if nums[i] != 0:
            if i != j:
                nums[j], nums[i] = nums[i], nums[j]
            j += 1
    print(nums)


nums1 = [0, 1, 0, 3, 12]
moveZeroes(nums1)  

nums2 = [0]
moveZeroes(nums2)  #
