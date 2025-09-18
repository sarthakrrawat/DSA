class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        ha = set(nums1)
        ha2 = set(nums2)
        l1 = []
        l2 = []
        for i in nums1:
            if i not in ha2:
                if i not in l1:
                    l1.append(i)
        for j in nums2:
            if j not in ha:
                if j not in l2:
                    l2.append(j)
        return [l1,l2]

    
        


        