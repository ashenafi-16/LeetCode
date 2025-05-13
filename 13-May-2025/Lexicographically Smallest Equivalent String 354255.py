# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = {chr(i):chr(i) for i in range(ord('a'),ord('z') + 1)}
        def find(x):
            while x != graph[x]:
                graph[x] = graph[graph[x]]
                x = graph[x]
            return graph[x]
        def union(x,y):
            root1 = find(x)
            root2 = find(y) 
            if root1 > root2:
                graph[root1] = root2
            else:
                graph[root2] = root1
        for i in range(len(s1)):
            union(s1[i],s2[i])
        ans = []
        for val in baseStr:
            ans.append(find(val))
        return ''.join(ans)