# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        count = defaultdict(list)
        length = 0
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                count[i].append(rooms[i][j])
        def get_neighbor(node):
            return count[node]
        visited =set()
        visited.add(0)
        def rec(val):
            nonlocal length
            if val not in visited:
                visited.add(val)
                length += 1
            for neighbor in get_neighbor(val):
                if neighbor not in visited:
                    rec(neighbor)
            return length 
            

        if rec(0) == (len(rooms) - 1):
            return True
        return False
        