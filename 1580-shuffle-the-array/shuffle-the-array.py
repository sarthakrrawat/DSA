class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        ans = []
        i = 0
        j = n 
        while j < 2*n:
            ans.append(nums[i])
            ans.append(nums[j])
            i += 1
            j += 1
        return ans
