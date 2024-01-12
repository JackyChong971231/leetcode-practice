from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sorted_prices = sorted(enumerate(prices), key=lambda x: x[1])
        left = 0
        right = len(prices) - 1
        i = 0
        while right > left:
            if sorted_prices[right][0] > sorted_prices[left][0]:
                return sorted_prices[right][1] - sorted_prices[left][1]
            if i % 2 == 0:
                left += 1
            else: 
                right -= 1
            i += 1



output = Solution.maxProfit(Solution, [7,1,5,3,6,4])
print(output)