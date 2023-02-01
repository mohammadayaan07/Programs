"""Input: s = "abc", t = "ahbgdc"
Output: true"""
class Solution(object):
    def isSubsequence(self, s, t):
        v=[]
        if len(s)==0 or len(t)==0:
            return True
        if len(s)==1:
            if s[0]in t:
                return True
            else:
                return False
        for i in range(len(s)):
            if s[i] in t:
                v.append(True)
            else:
                v.append(False)
        if len(set(v))==1:
            return True
        else:
            return False
    
s="acb"
t="ahbgdc"
S=Solution()
print(S.isSubsequence(s,t))