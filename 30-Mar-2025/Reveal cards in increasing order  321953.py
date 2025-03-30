# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        res = [0] * len(deck)
        
        index = deque(range(len(deck)))

        for m in deck:
            i = index.popleft()
            res[i] = m
            if index:
                index.append(index.popleft())
        return res