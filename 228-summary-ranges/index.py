from typing import List
class Solution:
    @classmethod
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if len(nums) == 0 :
            return []
        if len(nums) == 1 :
            res.append((nums[0], nums[0]))
        else :
            for idx, value in enumerate(nums):
                if idx > 0:
                    if value == tmp_previous + 1 :
                        high = value
                        tmp_previous = value
                        if idx == len(nums) - 1:
                            res.append((low, high))
                    else :
                        res.append((low, high))
                        # set new pair to current item
                        low, high, tmp_previous = value, value, value
                        if idx == len(nums) - 1:
                            res.append((value, value))

                else :
                    low = nums[0]
                    high = nums[0]
                    tmp_previous = value
        my_res = []
        for i in res :
            if i[0] == i[1]:
                my_res.append(str(i[0]))
            else :
                my_res.append(str(i[0]) +"->"+ str(i[1]))

        return my_res

print(Solution.summaryRanges(nums=[0,2,3,4,6,8,9]))
print(Solution.summaryRanges(nums=[0,1,2,4,5,7]))
print(Solution.summaryRanges(nums=[0,1,2,4,5,7,8]))
print(Solution.summaryRanges(nums=[0,1,2,4,5,7,9]))
print(Solution.summaryRanges(nums=[0]))
print(Solution.summaryRanges(nums=[1]))