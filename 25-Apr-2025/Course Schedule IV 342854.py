# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        ans = [False] * len(queries)
        for fir , sec in prerequisites:
            graph[sec].append(fir)
        pre_req = defaultdict(set) 
        def dfs(fir,temp,visited):

            
            visited.add(fir)
            for neigh in graph[fir]:
                if neigh not in visited:
                    visited.add(neigh)
                    pre_req[temp].add(neigh)

                    dfs(neigh,temp,visited)

        for fir in list(graph.keys()):
            dfs(fir,fir,set())
        for idx,(fir,sec) in enumerate(queries):
            if fir in pre_req[sec]:
                ans[idx] = True
        return ans
        