class Solution:
    def mergeTwoLists(self, list1, list2):
        if len(list1)>=len(list2):
            for i in list2:
                list1.append(i)
            list1.sort()
            return list1
        else:
            for i in list1:
                list2.append(i)
            list2.sort()
            return list2   
list1 = [1,2,4]
list2 = [1,3,4]
S=Solution()
print(S.mergeTwoLists(list1,list2))
