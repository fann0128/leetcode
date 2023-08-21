from typing import List
class Solution:
    @classmethod
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        
        for i in range(len(nums)):
            if nums[i] > 0:
                pass
            elif i != len(nums)-1:
                # make sure exist one step that can bypass this 0
                j = i-1 #0
                can_bypass = False
                while j >= 0:
                    if nums[j] > i-j: 
                        can_bypass = True
                        break
                    j -= 1
                if can_bypass :
                    pass 
                else:
                    return can_bypass

        return True

Solution.canJump(nums=[2,0,0])

