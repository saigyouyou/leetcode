#-- coding:utf-8--
# 大数+1问题，如果不用reverse()速度会快一些，代码逻辑上会复杂一些
class Solution(object):
    def plusOne(self, digits):
        digits.reverse()
        plus = True
        for i,ii in enumerate(digits):
            if ii+1>9:
                digits[i] = 0
            else:
                plus = False
                digits[i] = digits[i]+1
                break
        if plus == True:
            digits.append(1)
        digits.reverse()
        return digits