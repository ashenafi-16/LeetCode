# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        count = defaultdict(list)
        outdegree = defaultdict(int)
        dq = deque()
        ans = []
        for idx,val in enumerate(graph):
            for  t in val:
                count[t].append(idx)
                outdegree[idx] += 1
        for i in range(len(graph)):
            if outdegree[i] == 0:
                dq.append(i)
        while dq:
            node = dq.popleft()
            ans.append(node)
            for val in count[node]:
                outdegree[val] -= 1
                if outdegree[val] == 0:
                    dq.append(val)
        ans.sort()
        return ans
      