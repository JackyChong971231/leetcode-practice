from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        left = 1
        for i in range(len(nums)-1):
            
            ans[i+1] *= left * nums[i]
            left *= nums[i]
        right = 1
        for i in range(len(nums)-1,0,-1):
            ans[i-1] *= right * nums[i]
            right *= nums[i]
        return ans
    
        