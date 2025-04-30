# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap_val = []
        for i in range(1,len(heights)):
            if heights[i] > heights[i-1]:
                heappush(heap_val,abs(heights[i-1]-heights[i]))
                if len(heap_val) > ladders:
                    node = heappop(heap_val)
                    if node <= bricks:
                        bricks -= node
                    else:
                        return i-1
        return len(heights)-1
        

