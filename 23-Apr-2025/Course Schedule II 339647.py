# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        dq = deque()
        indegree = defaultdict(int)
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1    
        for i in range(numCourses):
            if indegree[i] == 0:
                dq.append(i)
        ans = []
        def bfs(dq):
            while dq:
                node = dq.popleft()
                ans.append(node)
                for neigh in graph[node]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 0:
                        dq.append(neigh) 
        bfs(dq)
        return ans if len(ans) == numCourses else []
