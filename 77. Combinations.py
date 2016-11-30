# -- coding:utf-8--
# 试了几次直接写都是TLE，只好参考了一下itertools的实现方法
# 使用迭代器和生成器结果速度惊人
class Solution(object):
    def combine(self, n, k):
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

        ret = combination( range(1,n+1), k )
        return list(ret)