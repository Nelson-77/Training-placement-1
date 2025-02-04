class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n > 1 and n not in seen:
            seen.add(n)
            v = 0
            while n > 0:
                v += pow(n % 10, 2)
                n = n // 10
            n = v
        return n == 1
