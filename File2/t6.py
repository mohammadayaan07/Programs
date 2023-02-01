class Solution(object):
    def averageValue(self, nums):
        nlst=[]
        for i in nums:
            if 3<i:
                if i%3==0:
                    nlst.append(i)
        l=len(nlst)
        print(nlst)
        if l==0:
            return 0
        elif l==1:
            return nlst[0]
        else:
            sm=0
            for i in nlst:
                sm=sm+i
            print(sm)
nums = [1,3,6,10,12,15]
S=Solution()
print(S.averageValue(nums))