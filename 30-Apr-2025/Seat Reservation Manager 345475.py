# Problem: Seat Reservation Manager - https://leetcode.com/problems/seat-reservation-manager/description/

class SeatManager:
    def __init__(self, n: int):
        self.arr = []
        for i in range(n):
            heappush(self.arr,i+1)
        
    
    def reserve(self) -> int:
        if self.arr:
            node = heappop(self.arr)
            return node
      
        

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.arr,seatNumber)
        

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)