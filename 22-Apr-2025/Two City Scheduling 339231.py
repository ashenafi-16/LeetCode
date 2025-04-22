# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ind_val = []
        for idx,(fir,sec) in enumerate(costs):
            ind_val.append((abs(fir-sec),idx))
        count_A = 0
        count_B = 0
        ans = 0
        n = len(costs)//2
        ind_val.sort(reverse= True)
        for val,i in ind_val:
            if count_A < n and costs[i][0] <= costs[i][1]:
                ans += costs[i][0]
                count_A += 1
            elif count_B < n and costs[i][0] >= costs[i][1]:
                ans += costs[i][1]
                count_B += 1
            elif count_B >= n:
                ans += costs[i][0]
                count_A += 1
            elif count_A >= n:
                ans += costs[i][1]
                count_B += 1

        return ans