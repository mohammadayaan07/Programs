class Solution:
    def threeSumClosest(self, nums, target) -> int:
        val1=target-2
        val2=target+2
        ls=[]
        for i in nums:
            if i>=val1 and i<=val2:
                ls.append(i)
        return sum(ls)
            
nums = [-1,2,1,-4]
target = 1
S=Solution()
print(S.threeSumClosest(nums,target))