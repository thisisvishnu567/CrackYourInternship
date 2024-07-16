from typing import List

def maxProfit(self, prices: List[int]) -> int:
    l,r = 0,1
    Max = 0

    while r<len(prices):
        if prices[l] < prices[r]: 
            Max = max(Max , prices[r] - prices[l])
        else:
            l=r
        r+=1
    return Max