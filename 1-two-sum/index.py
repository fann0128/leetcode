from typing import List, Dict
class Solution:
    @classmethod
    def twoSum(cls, nums: List[int], target: int):
        num_dict:Dict = {}
        for i in range(len(nums)) :
            if nums[i] in num_dict.keys() :
                num_dict[nums[i]].append(i)
            else :
                num_dict[nums[i]] = [i]
        
        for num in num_dict.keys() :
            pair_to_find = target - num
            if pair_to_find in num_dict.keys() :
                if pair_to_find != num :
                    return [num_dict[num][0], num_dict[pair_to_find][0]]
                elif len(num_dict[num]) > 1 :
                    return num_dict[num]

print(Solution.twoSum(nums=[3,2,4], target=6))