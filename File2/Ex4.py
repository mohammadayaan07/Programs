class Solution:
    def reverse(self, n: int) -> int:
        val=str(n)
        if val[0]=="-":
            n=int("-"+val[:0:-1])
            a=n
        else:
            a= val[::-1]
        if a >= -2147483648 and a<= 2147483647:
            return a
        else:
            return 0
    
x = 123
S=Solution()
print(S.reverse(x))