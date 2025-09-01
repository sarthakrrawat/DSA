class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = []
        for i in s:
            if i.isalpha() is True:
                l.append(i)
            else:
                l.pop()
        return ''.join(l)