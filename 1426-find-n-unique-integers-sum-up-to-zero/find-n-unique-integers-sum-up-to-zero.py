class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l = []
        if  n%2 == 0:
            for i in range(1,n/2 + 1):
                l.append(i)
                l.append(-i)
        else:
            for i in range(1,(n+1)/2):
                l.append(i)
                l.append(-i)
            l.append(0)
        return l

        