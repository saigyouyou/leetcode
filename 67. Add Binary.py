#-- coding:utf-8--
# 二进制加法
class Solution(object):
    def addBinary(self, a, b):
        a = list(a)
        a.reverse()
        b = list(b)
        b.reverse()
        c = []
        plus = 0
        i = 0
        ma = len(a)
        mb = len(b)
        while i < ma or i < mb:
            if i >= ma:
                x = 0
            else:
                x = int(a[i])
            if i >= mb:
                y = 0
            else:
                y = int(b[i])
            tmp = x + y + plus
            if tmp == 0:
                c.append('0')
                plus = 0
            elif tmp == 1:
                c.append('1')
                plus = 0
            elif tmp == 2:
                c.append('0')
                plus = 1
            elif tmp == 3:
                c.append('1')
                plus = 1
            i = i+1
        if plus == 1:
            c.append('1')
        c.reverse()
        return ''.join(c)