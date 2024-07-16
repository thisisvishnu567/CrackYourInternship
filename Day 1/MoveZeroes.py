from typing import List

def solution(nums: List[int]) -> None:
    i,j = 0,0
    while j < len(nums):
        if nums[j] != 0:
            nums[i] = nums[j]
            i+=1
        j+=1
        
    while i < len(nums):
        nums[i] = 0
        i+=1


def main():
    nums = [0,1,0,2,3,4]
    solution(nums)
    print(nums)

if __name__ == "__main__":
    main()