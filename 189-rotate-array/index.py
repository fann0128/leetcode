from typing import List
class Solution:
    @classmethod
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length_of_array = len(nums)
        
        nums[:0] = nums[-k:]
        
        x_item_to_del = len(nums)-length_of_array

        del nums[-x_item_to_del:]
        print(nums)
        # for i in range(k):
        #     item = nums.pop()
        #     nums.insert(0, item)

Solution.rotate(nums=[1,2,3,4,5,6,7], k=3)