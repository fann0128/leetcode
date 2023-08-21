from typing import List
class Solution:
    @classmethod
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] > len(nums)-1:
            return 1
        cur_position = 0
        step = 0
        while cur_position < len(nums) - 1:
            max_can_jump = nums[cur_position]
            if max_can_jump == 1:
                cur_position += 1
            else :
                far_postion = cur_position
                postion_should_jump_to = cur_position
                for i in range(max_can_jump+1) :
                    if cur_position + i < len(nums) :
                        if nums[cur_position + i] > 0 :
                            temp_far = cur_position + nums[cur_position + i] + i + 1
                            if temp_far > far_postion:
                                far_postion = temp_far
                                postion_should_jump_to = cur_position + i
                cur_position = postion_should_jump_to
            step += 1
        
        return step

print(Solution.jump(nums=[1,3,2]))
# print(Solution.jump(nums=[3,2,2,0,4]))
# print(Solution.jump(nums=[1,2,0,1]))

# print("all 1 :")
# print(Solution.jump(nums=[1,1,1,1]))
# print(Solution.jump(nums=[1,1,1]))
# print(Solution.jump(nums=[1,1]))

