
class Solution(object):
    def isIsomorphic(self, s, t):
        a=list(zip(s,t))
        if len(a)<=3:
            for i in range(len(a)):
                if str(a[i]) == str(a[i+1]):
                    return True 
                else:
                    return False
            
           
        else:
            for i in range(len(a)):
                if str(a[i]) in [str(val) for val in a[i+1::]]:
                    return True 
                else:
                    return False
            
s="mom"
t="dad"
v=Solution()
ab=v.isIsomorphic(s,t)
print(ab)
