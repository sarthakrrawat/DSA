class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        import math
        if math.fabs(z-x) > math.fabs(z-y):
            return 2
        elif math.fabs(z-y) > math.fabs(z - x):
            return 1
        else:
            return 0