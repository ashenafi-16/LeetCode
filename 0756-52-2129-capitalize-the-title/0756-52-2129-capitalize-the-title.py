class Solution:
    def capitalizeTitle(self, title: str) -> str:
        splited= title.lower().split()
        for i in range(len(splited)):
            if len(splited[i])> 2:
                splited[i] = splited[i].title()
        return " ".join(splited)
