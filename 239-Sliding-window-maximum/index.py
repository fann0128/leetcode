from typing import List
from collections import deque

class Solution:
    @classmethod
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        my_queue = deque()
        res = []
        for i in range(k):
            while my_queue and my_queue[-1] < nums[i]:
                my_queue.pop()
            my_queue.append(nums[i])
        res.append(my_queue[0])

        for i in range(len(nums)-k):
            if nums[i] == my_queue[0]:
                my_queue.popleft()
            while my_queue and my_queue[-1] < nums[i+k]:
                my_queue.pop()
            my_queue.append(nums[i+k])
            res.append(my_queue[0])
        
        return res

print(Solution.maxSlidingWindow(nums=[1,3,-1,-3,5,3,6,7], k=3) == [3,3,5,5,6,7])