
def isPalindrome(self, s: str) -> bool:
    k=''
    for i in s:
        if i.isalnum():
            if i.isalpha():
                k+=i.lower()
            else:
                k+=i
    x=len(k)
    if x==1:
        return True
    left=0
    right=x-1
    
    while left<right:
        if k[left]!=k[right]:
            return False
        
        left+=1
        right-=1
    
    return True

