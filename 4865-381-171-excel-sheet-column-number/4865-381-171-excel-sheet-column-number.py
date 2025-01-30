class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle = columnTitle[::-1]
        total = 0
        length = len(columnTitle)
        for i in range(length):
            val = ord(columnTitle[i]) - ord("A") + 1
            total += pow(26,i)
            total += (val-1)*pow(26,i)
        return total