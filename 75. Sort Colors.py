#-- coding:utf-8--
# 实际上就是数区块的数量，可以扫一遍写一遍
# 但是有个更巧妙的写法，扫的同时写数据
class Solution(object):
    def sortColors(self, nums):
        i = -1
        j = -1
        k = -1
        n = len(nums)
        for x in xrange(n):
            if nums[x] == 0:
                k += 1
                j += 1
                i += 1
                nums[k] = 2
                nums[j] = 1
                nums[i] = 0
            elif nums[x] == 1:
                k += 1
                j += 1
                nums[k] = 2
                nums[j] = 1
            else:
                k += 1
                nums[k] = 2