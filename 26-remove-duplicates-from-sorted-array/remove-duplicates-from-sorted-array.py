class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #sarthak
        m = -float('inf')
        i = 0
        while i < len(nums):
            if nums[i] == m:
                nums.pop(i)
            else:
                m = nums[i]
                i += 1
        return len(nums)
