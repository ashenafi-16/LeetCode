class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        res = []
        res.extend([int(item) for item in s.split(" ") if item.isdigit()])
        check = res[0]
        for i in range(1,len(res)):
            if check < res[i]:
                check = res[i]
            else:
                return False
        return True