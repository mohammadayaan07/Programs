class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        val=(nums1+nums2)
        val.sort()
        l=len(val)
        if l%2==0:
            sm=l//2
            print(val[sm-1])
            sm1=sm-1
            mean=(val[sm1]+val[sm])
            mean=mean/2
        else:
            sm=l//2
            mean=val[sm]
        return mean
nums1 = [1,2]
nums2 = [3,4]

S=Solution()
print(S.findMedianSortedArrays(nums1,nums2))
