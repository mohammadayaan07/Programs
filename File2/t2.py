class Solution(object):
    def deleteDuplicates(self, head):
        h=set(head)
        d=list(h)
        return d
head = [1,1,2,3,3]
S=Solution()
print(S.deleteDuplicates(head))