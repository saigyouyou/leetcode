#-- coding:utf-8--
# 牛顿就迭代法
class Solution(object):
    def mySqrt(self, x):
        a1 = x
        if x == 0: return 0
        while True:
            a2 = 0.5*(a1+ x/a1)
            if abs(a2 - a1) <= 0.0001:
                return int(a2)
            a1 = a2