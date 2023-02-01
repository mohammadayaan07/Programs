class Solution(object):
    def plusOne(self, digits):
        l=len(digits)
        sm=0
        for i in range(l):
            val=digits[i]
            sm=sm*10+val
        sm=sm+1
        Frt=str(sm)
        F=list(Frt)
        lst=[]
        for val in F:
            lst.append(int(val))
        return lst
        
digits=[9]
S=Solution()
print(S.plusOne(digits))
