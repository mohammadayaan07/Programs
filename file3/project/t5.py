class Solution(object):
    def addTwoNumbers(self, l1, l2):
        a=0
        for i in range(len(l1)):
            a=l1[i]+a
            print(a)
        print(a)
S=Solution()
l1 = [2,4,3]
l2 = [5,6,4]
S.addTwoNumbers(l1,l2)