from typing import List
class Solution:
    @classmethod
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_station = len(gas)
        if gas == cost :
            return 0

        if sum(gas) < sum(cost) :
            return -1
            
        for i in range(len(gas)):
            gas[i] -= cost[i]
         
        fuel = 0
        ans = 100002
        for start_at in range(total_station) :
            fuel += gas[start_at]
            if fuel < 0:
                fuel = 0
                ans = 100002
            else :
                ans = min(start_at, ans)
            
        return ans

print(Solution.canCompleteCircuit(gas=[1,2,3,4,5], cost=[3,4,5,1,2]))
print(Solution.canCompleteCircuit(gas=[2,3,4], cost=[3,4,3]))