#to find lsit index of sum of number which is equal given number:
"""s=[1,4,6,2,3,5]
n=8
def chk(lst):
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if n==s[i]+s[j]:
                return i ,j 
lt=chk(s)
print(lt)
"""

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            if nums[i]+nums[i+1]==target:
                return i,i+1
nums=[2,7,11,15]
target=9
s=Solution()
print(s.twoSum(nums,target))