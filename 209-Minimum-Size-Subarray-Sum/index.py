from typing import List
class Solution:
    @classmethod
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, current_sum = 0, 0
        min_length = float('inf')

        for r in range(len(nums)):
            current_sum += nums[r]
            if current_sum >= target:
                min_length = min(r-l+1, min_length)
                while(current_sum >= target) :
                    current_sum -= nums[l]
                    l += 1
                    if current_sum >= target:
                        min_length = min(r-l+1, min_length)
        
        if min_length == float('inf'):
            return 0
        return min_length

print(Solution.minSubArrayLen(target=7, nums=[2,3,1,2,4,3]))