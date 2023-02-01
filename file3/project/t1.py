class Solution(object):
    def runningSum(self, nums):
        ls=[]
        ls.append(nums[0])
        for i in range(len(nums)-1):
            ls.append(ls[i]+nums[i+1])
        print(ls)
inp=[1,1,1,1,1]
s=Solution()
s.runningSum(inp)