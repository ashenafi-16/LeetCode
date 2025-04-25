# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        ans = [0] * len(quiet)
        for i in range(len(ans)):
            ans[i] = i
        for a , b in richer:
            graph[b].append(a)
        def bfs(index,visited,dq,min_index):
            dq.append(index)
            visited.add(index)
            while dq:
                node = dq.popleft()
                
                if quiet[min_index] > quiet[node]:
                    min_index = node
                for neigh in graph[node]:
                    if neigh not in visited:
                        dq.append(neigh)
                        visited.add(neigh)
            return min_index
        for i in list(graph.keys()):
            # if richer:
            ans[i] = bfs(i,set(),deque(),i)
        return ans