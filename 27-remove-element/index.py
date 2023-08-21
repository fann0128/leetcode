from typing import List
class Solution:
    @classmethod
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for cur_index in range(len(nums)) :
            if nums[cur_index] == val :
                next_index = cur_index + 1
                # find the next not val item and swap
                while next_index < len(nums):
                    if nums[next_index] != val :
                        temp = nums[next_index] 
                        nums[next_index] = nums[cur_index]
                        nums[cur_index] = temp
                        break
                    else :
                        next_index = next_index + 1
        for i in nums[::-1] :
            if i == val:
                k = k + 1
            else :
                break
        return len(nums) - k

Solution.removeElement(nums=[3,2,2,3], val=3)