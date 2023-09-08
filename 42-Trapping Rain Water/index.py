from typing import List
class Solution:
    @classmethod
    def trap(self, height: List[int]) -> int:
        total_water = 0

        n = len(height)
        max_left = [0]*n
        max_right = [0]*n
        
        max_left[0] = height[0]
        for i in range(1, n) :
            max_left[i] = max(max_left[i-1], height[i])
        
        max_right[n-1] = height[-1]

        for i in range(n-2, -1, -1):
            max_right[i] = max(height[i], max_right[i+1])
        
        for i in range(n):
            tmp_min = min(max_left[i], max_right[i])
            if height[i] < tmp_min:
                total_water += tmp_min - height[i]
            
        return total_water
    

print(Solution.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]) == 6)
print(Solution.trap(height = [4,2,0,5,2,5]) == 9)
print(Solution.trap(height = [0,1,0,2,1,0,1,3,2,1,2,5]) == 9)
print(Solution.trap(height = [9,1,0,2,1,0,1,3,2,1,2,5]) == 37)
print(Solution.trap(height = [9,1,0,2,1,10,1,3,2,1,2,5]) == 48)
print(Solution.trap(height = [4,9,4,5,3,2]) == 1)
print(Solution.trap(height = [10,0,9,0,8,0,7,6,0,5,0,4,0,3,0,2,0,1]) == 39)
print(Solution.trap(height = [1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0,10]) == 45)
print(Solution.trap(height = [1]) == 0)

# Brutual solution 😅 Time limit exception
# def trap(self, height: List[int]) -> int:
#         total_water = 0
#         ptr, l_ptr, r_ptr = 0, 0, 0
#         while ptr < len(height) - 1:
#             # if l_ptr < len(height) - 1:
#             if height[ptr] > height[ptr + 1]:
#                 l_ptr, r_ptr = ptr, ptr
#                 went_down, went_up = False, False
#                 # go find the lowest point
#                 while r_ptr < len(height) - 1 and height[r_ptr] >= height[r_ptr + 1]:
#                     r_ptr += 1
#                     ptr += 1
#                     went_down = True

#                 # go find the next highest point
#                 tmp_next_heigh_ptr = r_ptr
#                 while r_ptr < len(height) - 1 and height[r_ptr] <= height[l_ptr]:
#                     if height[r_ptr] > height[r_ptr + 1] and height[r_ptr] > height[tmp_next_heigh_ptr]:
#                         tmp_next_heigh_ptr = r_ptr
#                     r_ptr += 1
#                     ptr += 1
#                     went_up = True
                
#                 if r_ptr == len(height) - 1 and height[r_ptr] < height[l_ptr]:
#                     r_ptr = r_ptr if height[r_ptr] > height[tmp_next_heigh_ptr] else tmp_next_heigh_ptr
#                     ptr = r_ptr

#                 if went_down and went_up:
#                     width = r_ptr-l_ptr-1
#                     trap_height = min(height[l_ptr], height[r_ptr])
#                     maximum_water = width * trap_height
#                     for i in range(l_ptr+1, r_ptr):
#                         maximum_water -= min(height[i], trap_height)
#                     total_water += maximum_water
#             else:
#                 ptr += 1
#         return total_water