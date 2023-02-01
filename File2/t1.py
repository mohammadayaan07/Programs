class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for v in range(i+1,len(nums)):
                if nums[i]+nums[v]==target:
                    return i,v
nums=[3,2,3]
target=6
s=Solution()
print(s.twoSum(nums,target))
