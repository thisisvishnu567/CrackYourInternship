from typing import List

def solution(nums : List[int]) -> int:
    i = 1
    for j in range(1,len(nums)):
        if nums[j] != nums[j-1]:
            nums[i] = nums[j]
            i+=1
    return i


nums = [0,0,1,1,1,2,2,3,3,3,4]
solution(nums)
for i in nums:
    print(nums[i] , end=" ")