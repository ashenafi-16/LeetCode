class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewals_count = Counter(jewels)
        stones_count = Counter(stones)
        count = 0
        for ch,val in jewals_count.items():
            if ch in stones_count:
                count += (stones_count[ch] * val)
        return count
