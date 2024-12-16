class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version2 = version2.split(".")
        version1 = version1.split(".")
        length = max(len(version1), len(version2))
        for i in range(length):
            v1 = int(version1[i]) if i < len(version1) else 0
            v2 = int(version2[i]) if i < len(version2) else 0
            
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
            
        return 0
