from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = nums[0]
        current_subarray_max = nums[0]
        i = 1
        while i < len(nums):
            # if nums[i+1] >= nums[i] + current_max_subarray:
            #     current_max_subarray = nums[i+1]
            #     i += 1
            # else:
            #     if nums[i] >= 0 :
            #         current_max_subarray += nums[i]
            #     else:
            #         if nums[i] + nums[i+1] >= 0:
            #             current_max_subarray += nums[i]
            #         else:
            
            
            
            
            current_subarray_max = max(current_subarray_max+nums[i], nums[i])  
            max_subarray = max(current_subarray_max, max_subarray)
            
        
                        
                        
                        
                    
                    
            i += 1
                
            
        return max_subarray
    
output = Solution.maxSubArray(Solution, [-2,1,-3,4,-1,2,1,-5,4])
print(output)