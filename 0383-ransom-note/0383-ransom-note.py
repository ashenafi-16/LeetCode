class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = Counter(ransomNote)
        magazi = Counter(magazine)
        for ch,val in ransom.items():
            if ch in magazi and val <= magazi[ch]:
                continue
            else:
                return False
        return True