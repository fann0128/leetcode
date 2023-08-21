from typing import List
class Solution:
    @classmethod
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # if len(points) == 1 :
        #     return 1
        # points.sort()
        # number_of_shot = 0
        # while len(points) > 0:
        #     # first item
        #     max_shot = 0

        #     for i in range(points[0][0], points[0][1]+1) :
        #         tmp = 0
        #         for j in range(len(points)):
        #             if points[j][0] <= i <= points[j][1] :
        #                 tmp += 1
        #             else :
        #                 break
        #         if tmp > max_shot :
        #             max_shot = tmp
            
        #     # shot on the max_shot_pos
        #     number_of_shot += 1
        #     points = points[max_shot:]
        # return number_of_shot

        if len(points) == 0:
            return 0
        
        # Sort the intervals based on their end points
        points.sort(key=lambda x: x[1])
        
        # Initialize the variables
        shot_end = points[0][1]
        number_of_shots = 1
        
        # Iterate through the sorted intervals
        for interval in points:
            start, end = interval
            # If the interval doesn't overlap with the current shot, update the shot
            if start > shot_end:
                number_of_shots += 1
                shot_end = end
        
        return number_of_shots

# print(Solution.findMinArrowShots(points=[[10,16],[2,8],[1,6],[7,12]]))
# print(Solution.findMinArrowShots(points=[[1,2],[2,3],[3,4],[4,5]]))
print(Solution.findMinArrowShots(points=[[4289383,51220269],[81692777,96329692],[57747793,81986128],[19885386,69645878],[96516649,186158070],[25202362,75692389],[83368690,85888749],[44897763,112411689],[65180540,105563966],[4089172,7544908]]))
# print(Solution.findMinArrowShots(points=[[0,9],[1,8],[7,8],[1,6],[9,16],[7,13],[7,10],[6,11],[6,9],[9,13]]))


# [[4289383,51220269],[81692777,96329692],[57747793,81986128],[19885386,69645878],[96516649,186158070],[25202362,75692389],[83368690,85888749],[44897763,112411689],[65180540,105563966],[4089172,7544908]]