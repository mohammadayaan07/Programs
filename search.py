class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        if x==str(x[::-1]):
            return True
        else:
            return False
S=Solution()
x=-121
print(S.isPalindrome(x))


x=input("enter anything")
if x.lower()==x[::-1].lower():
    print("IS palen")
else:
    print("IS not")