class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_count = Counter(text)
        ballon = Counter('balloon')
        compare = float('inf')
        for ch,val in ballon.items():
            if ch in text_count:
                if compare > (text_count[ch])//val:
                    compare = (text_count[ch])//val
            else:
                return 0
        return compare
