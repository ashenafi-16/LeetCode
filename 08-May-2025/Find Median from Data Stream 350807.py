# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heappush(self.small,num)
        if len(self.small) > (len(self.large) + 1):
            node = heappop(self.small)
            heappush(self.large,-1 * node)
        elif self.large and self.small[0] < -1 * self.large[0]:
            node = heappop(self.small)
            heappush(self.large,-1 * node)
        if len(self.large) > (len(self.small) + 1):
            node = heappop(self.large)
            heappush(self.small,-1 * node)

    def findMedian(self) -> float:
        if (len(self.small) + len(self.large)) % 2 == 0:
            ans = (self.small[0] + (-1 * self.large[0]))/2
            return ans
        elif len(self.small) > len(self.large):
            return self.small[0]
        elif len(self.large) > len(self.small):
            return -1 * self.large[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()