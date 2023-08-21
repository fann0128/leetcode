from typing import List
class Solution:
    @classmethod
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2:
            return [1,2]
        res = []
        for i in range(len(numbers)) :
            current_num = numbers[i]
            number_to_find = target - current_num
            number_to_find_index = None
            l, r = i+1, len(numbers)-1 # 1,2
            while l <= r:
                mid_index = (l+r)//2 # 1
                if numbers[mid_index] < number_to_find:
                    l = mid_index + 1
                elif numbers[mid_index] > number_to_find:
                    r = mid_index - 1 
                else :
                    number_to_find_index = mid_index
                    break
            
            if number_to_find_index is not None :
                res = [i+1, number_to_find_index+1]
                break

        return res
    
print(Solution.twoSum(numbers=[5,25,75], target=100))