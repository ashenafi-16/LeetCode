class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        power = []
        x = int(log(n,3))
        while x >= 0 and n != 0:
            x = int(log(n,3))
            if (x + 1) - log(n,3) <= pow(10,-6):
                x+=1

            while x in power:
                x -= 1
            
            n = n - pow(3,x)
            power.append(x) 
            if n == 0:
                return True
        print(x, n)  
        print(power)
        return False

            
