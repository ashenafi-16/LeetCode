# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        arr = [float('inf')] * n
        for a,b,val in times:
            graph[a-1].append((b-1,val))
        dq = deque()

        def bfs(node):
            dq.append((node,0))
            arr[node] = 0
            while dq:
                a,val = dq.popleft()
                for neigh,weight in graph[a]:
                    if arr[neigh] > (arr[a] + weight):
                        arr[neigh] = (arr[a] + weight)
                    
                        dq.append((neigh,weight))

        bfs(k-1)
        return max(arr) if max(arr) != float('inf') else -1