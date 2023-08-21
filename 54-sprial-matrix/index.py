from typing import List
class Solution:
    @classmethod
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        def runCircle(x_start, x_end, y_start, y_end, res):
            if x_start+1 < x_end and y_start+1 < y_end:
                # top
                for x in range(x_start, x_end - 1):
                    res.append(matrix[y_start][x])
                # right
                for y in range(y_start, y_end - 1):
                    res.append(matrix[y][x_end-1])
                # bottom
                for x in reversed(range(x_start+1, x_end)):
                    res.append(matrix[y_end-1][x])
                # left
                for y in reversed(range(y_start+1, y_end)):
                    res.append(matrix[y][x_start])
                runCircle(x_start+1, x_end-1, y_start+1, y_end-1, res)
            elif y_start + 1 == y_end and x_start + 1 < x_end:
                # only loop on x
                for x in range(x_start, x_end):
                    res.append(matrix[y_start][x])
            elif x_start + 1 == x_end and y_start + 1 < y_end:
                # only loop on y
                for y in range(y_start, y_end):
                    res.append(matrix[y][x_end-1])

        runCircle(0, len(matrix[0]), 0, len(matrix), res)

        if len(matrix[0]) == len(matrix) and len(matrix[0])%2==1 and len(matrix)%2==1:
            res.append(matrix[len(matrix)//2][len(matrix[0])//2])

        return res


print(Solution.spiralOrder(matrix=[[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))
# print(Solution.spiralOrder(matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

