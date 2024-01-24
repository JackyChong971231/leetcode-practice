from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_ind = 0
        end_ind = len(nums)-1

        while end_ind - start_ind > 0:
            left_end_ind = (start_ind + end_ind) // 2
            right_start_ind = left_end_ind + 1
            # check Left
            left_start_value, left_end_value = nums[start_ind]-target, nums[left_end_ind]-target
            right_start_value, right_end_value = nums[right_start_ind]-target, nums[end_ind]-target            
            if left_start_value <= left_end_value < 0 or 0 < left_start_value <= left_end_value or left_start_value > 0 > left_end_value:
                start_ind = right_start_ind
                next
            if 0 < right_start_value <= right_end_value or right_start_value <= right_end_value < 0 or right_start_value > 0 > right_end_value:
                end_ind = left_end_ind
                next
        if nums[start_ind]-target == 0: return start_ind
        elif nums[end_ind]-target == 0: return end_ind
        else: return -1
        

solution = Solution()
print(solution.search([4,5,6,7,0,1,2], 1))