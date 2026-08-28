'''
You are given an integer array prices where
prices[i] is the price of NeetCoin on the ith day.


You may choose a single day to buy one NeetCoin
and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may 
choose to not make any transactions, in which case
the profit would be 0. <- if the maximum profit is < 0
just set it to 0
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        start = 0
        end = start + 1
        while end < len(prices):
            if prices[end] < prices[start]:
                start = end
            else:
               maximum = max(maximum, prices[end] - prices[start])
            end += 1 
        return maximum


        