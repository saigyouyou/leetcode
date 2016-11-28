#--coding:utf8--
#康托展开:全排列的一种哈希表示
#I = a_n*(n-1)!+a_(n-1)*(n-2)!+...+a_i*(i-1)!+...+a_2*1!+a_1*0!
#注意逆运算是以k-1开始算
class Solution(object):
    def getPermutation(self, n, k):
        fac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320]
        tmp = []
        i = n - 1
        k = k - 1
        while i > 0:
            tmp.append(k / fac[i])
            k = k % fac[i]
            i = i - 1
        n_list = [str(i) for i in range(1,n+1)]
        ret = []
        for i in tmp:
            ret.append(n_list[i])
            del n_list[i]
        ret.append(n_list[0])
        return ''.join(ret)