# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        
        result = defaultdict(list)
        ans = 0
        stk = []
        for employee in employees:
            result[employee.id].append(employee.importance)
            result[employee.id].append(employee.subordinates)
        def get_neighbors(node):
            return result[node][1]
        def rec(idx):
            nonlocal ans
            stk = [idx]
            
            visit = set()
            while stk:
                node = stk.pop()
                
                if node not in visit:
                    ans += result[node][0]
                    visit.add(node)
                    
                    for neighbor in get_neighbors(node):
                        if neighbor not in visit:
                            stk.append(neighbor)
            return ans

           


        for idx,value in result.items():
            
            if idx == id:        
                return rec(idx)
