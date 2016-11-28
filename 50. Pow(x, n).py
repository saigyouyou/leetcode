class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1/self.myPow(x,-n)
        if n == 0:
            return 1
        if n == 1:
            return x
        else:
            n1 = n/2
            n2 = n%2
            tmp = self.myPow(x, n1)
            return tmp*tmp*self.myPow(x, n2)