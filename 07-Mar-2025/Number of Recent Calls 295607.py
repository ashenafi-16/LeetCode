# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.dq = deque()

    def ping(self, t: int) -> int:
        self.dq.append(t)
        i = 0
        while i < len(self.dq):
            if (t-3000 ) <= self.dq[i] <= t:
                pass
            else:
                self.dq.popleft()
                i -= 1
            i += 1
        return len(self.dq)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)