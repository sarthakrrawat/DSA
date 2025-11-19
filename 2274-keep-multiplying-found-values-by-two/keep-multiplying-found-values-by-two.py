class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        a = 0
        nums1 = sorted(nums)
        for i in nums1:
            if i == original:
                original = i*2
                a +=1
        return original
                