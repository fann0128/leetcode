from typing import List
class Solution:
    @classmethod
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] < target:
                l += 1
            else :
                r -= 1
        
        return [l+1,r+1]

print(Solution.twoSum(numbers=[5,25,75], target=100))