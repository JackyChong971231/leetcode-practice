from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        current = nums
        while len(current) > 1:
            middle_index = len(current)//2
            remainder = len(current)%2
            left = current[:middle_index]
            right = current[-(middle_index + remainder):]
            if left[-1] < left[0]: current = left
            elif right[-1] < right[0]: current = right
            elif left[0] < right[0]: return left[0]
            elif right[0] < left[0]: return right[0]
        return current
    
solution = Solution()
print(solution.findMin([3,4,5,1,2]))