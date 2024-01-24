from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Solution 3
        ##### nums = [ 6, 0, 2, -5, 3, -4 ]
        watchingMin = nums[0]
        watchingMax = nums[0]
        globalMax = nums[0]

        for num in nums[1:]:
            value1, value2 = watchingMin*num, watchingMax*num
            watchingMax = max(value1, value2, num)
            watchingMin = min(value1, value2, num)

            globalMax = max(globalMax, watchingMax)

        return globalMax
    

output = Solution.maxProduct(Solution, [6,0,2,-5, 3, -4])
print(output)