class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(1,n/2 + 1):
            if '0' in str(i):
                continue
            else:
                if '0' not in str(n - i):
                    return [i,n -i]
                else:
                    continue
        return null
