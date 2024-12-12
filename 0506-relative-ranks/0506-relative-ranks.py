class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sort_score = sorted(score,reverse=True)
        length = len(score)
        count = length - 1
        for i in range(length-1,-1,-1):
            index = sort_score.index(score[i])
            if index == 0:
                score[i] = "Gold Medal"
            elif index == 1:
                score[i] = "Silver Medal"
            elif index == 2:
                score[i] = "Bronze Medal"
            else:
                score[i] = str(index+1)
    
        return score