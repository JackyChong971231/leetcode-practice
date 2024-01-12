from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            valueNeeded = target - num
            if hashmap.get(valueNeeded) == None:
                hashmap[num] = i
            else:
                return [i, hashmap[valueNeeded]]
            
output = Solution.twoSum(Solution, [2,7,11,15], 9)
print(output)

'''
ChatGPT solution
    - O(n)
''' 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i

sorted_nums = sorted(enumerate([7,2,8,4,11,15]), key=lambda x: x[1])
print(sorted_nums)