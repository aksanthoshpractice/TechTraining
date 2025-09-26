class Solution:
    def isHappy(self, n: int) -> bool:
        seen=[]
        while True:
            if n in seen and n!=1:
                return False
            if n==1:
                return True
            seen.append(n)
            t=0
            while True:
                t+=(n%10)**2
                n=n//10
                if n==0:
                    break
            n=t
        return False

s=Solution()
n=int(input("Enter a Number:"))
print(s.isHappy(n))
