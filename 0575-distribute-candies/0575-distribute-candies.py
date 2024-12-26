class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        if len(set(candyType) )< n/2:
            return len(set(candyType))
    
        return n//2