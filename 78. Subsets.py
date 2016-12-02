# -- coding:utf-8--
# 使用77的combination很简单就能做出来
class Solution(object):
    def subsets( self, nums ):
        def combination(iter, k):
            n = len(iter)
            if k > n:
                return
            indices = range(k)
            yield [iter[i] for i in indices]
            while True:
                for i in reversed(range(k)):
                    if indices[i] != i + n - k:
                        break
                else:
                    return
                indices[i] += 1
                for j in range(i+1, k):
                    indices[j] = indices[j-1] + 1
                yield [iter[i] for i in indices]
        n = len(nums)
        ret = []
        for k in xrange(n,-1,-1):
            ret += combination(nums,k)
        return ret