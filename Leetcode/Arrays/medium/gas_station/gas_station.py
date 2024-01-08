class Solution:
    def find_starts(self, gas, cost):
        starts = []
        for i in range(len(gas)):
            if cost[i] <= gas[i]:
                starts.append(i)
        return starts
    
    def validate_route(self, start, gas, cost):
        fuel = gas[start] - cost[start]
        location = start
        while(fuel >= 0):
            if location == len(gas) -1:
                location = 0
            else:
                location += 1
            if location  == start:
                return True
            fuel += gas[location] - cost[location]
        return False

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        starts = self.find_starts(gas, cost)
        for i in starts:
            if self.validate_route(i, gas, cost) == True:
                return i
        return -1