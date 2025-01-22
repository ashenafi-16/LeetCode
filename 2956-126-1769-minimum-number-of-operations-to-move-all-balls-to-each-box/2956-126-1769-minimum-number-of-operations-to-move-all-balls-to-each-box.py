class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n

        count = 0  
        cost = 0   
        for i in range(n):
            answer[i] += cost
            count += int(boxes[i])  
            cost += count       
        count = 0
        cost = 0
        for i in range(n - 1, -1, -1):
            answer[i] += cost
            count += int(boxes[i])  
            cost += count         

        return answer
