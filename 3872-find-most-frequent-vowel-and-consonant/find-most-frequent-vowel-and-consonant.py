class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        vowels = 'aeiou'

        maxv = 0
    
        for j in vowels:
            try:
                if d[j] > maxv:
                    maxv = d[j]
                del d[j]
            except:
                continue
        maxc = max(d.values()) if d else 0
        return maxv + maxc