# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        graph = {chr(i):chr(i) for i in range(ord('a'),ord('z') + 1)}
        size = [1] * 26
        def find(x):
            while x != graph[x]:
                graph[x] = graph[graph[x]]
                x = graph[x]
            return graph[x]

        def union(x,y):
            root1 = find(x)
            root2 = find(y)
           
            if size[(ord(root1) - ord('a'))] > (ord(root2) - ord('a')):
                graph[root1] = root2
                size[(ord(root1) - ord('a'))] += size[(ord(root2) - ord('a'))]
            else:
                graph[root2] = root1
                size[(ord(root2) - ord('a'))] += size[(ord(root1) - ord('a'))]
        not_equal = []
        for val in equations:
            if val[1] == '=':
                union(val[0],val[3])
            else:
                not_equal.append([val[0],val[3]])
        for fir ,sec in not_equal:
            if find(fir) == find(sec):
                return False         
        return True