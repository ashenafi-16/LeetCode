# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.array = []
        self.pos = 0
        self.iterate = 0

    def add(self, num: int) -> None:
        self.iterate += 1
        if num == 0:
            self.pos = self.iterate
        self.array.append(num* self.array[-1] if self.array and self.array[-1] != 0 else num)
        
    def getProduct(self, k: int) -> int:
        
        if self.pos - 1 >= (self.iterate - k):
            return 0
        return self.array[-1]//self.array[-(k+1)] if k < len(self.array) and self.array[-(k+1)] != 0 else self.array[-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)