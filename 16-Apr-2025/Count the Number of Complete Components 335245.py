# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        count = defaultdict(list)
        res = 0
        def get_neighbor(node):
            nonlocal max_node
            nonlocal min_node
            max_node = max(max_node,len(count[node])) 
            min_node = min(min_node,len(count[node]))
            return count[node]
        for fir,sec in edges:
            count[fir].append(sec)
            count[sec].append(fir)
        
        visited = set()
        def rec(key):
            nonlocal count_edge
            if key not in visited:
                visited.add(key)
                count_edge += 1
                
            for neighbor in get_neighbor(key):
                if neighbor not in visited:
                    rec(neighbor)
        ans = 0
        for key in range(n):
            min_node = float("inf")
            max_node = float('-inf')
            count_edge = 0
            if key not in visited:
                rec(key)
                if max_node == min_node == count_edge - 1:
                    ans += 1
        return ans

            