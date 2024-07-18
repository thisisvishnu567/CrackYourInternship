def solution(nums , target):
    prevMap = {} #stores Value : index

    for i , n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff] , i]
        prevMap[n] = i
        return