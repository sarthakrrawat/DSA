class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        for i in range(len(nums)):
            for j in str(nums[i]):
                s += int(j)
            if s == i:
                return i
            s = 0
        return -1
