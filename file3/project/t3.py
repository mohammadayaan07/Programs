"""Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"""

class Solution(object):
    def reverseOnlyLetters(self, s):
        l=len(s)
        if "!" in s:
            s=s[-2::-1]+"!"
            return s
        else:
            s=s[::-1]
            return s
s="Test1ng-Leet=code-Q!"
S=Solution()
print(S.reverseOnlyLetters(s))

