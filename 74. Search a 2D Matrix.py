#-- coding:utf-8--
# 注意二分法处理时，左右指针差1时就要结束循环，否则可能出现死循环
# 结束循环后需判定到底是落在两行中的左边还是右边
class Solution(object):
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        ni = 0
        nj = n-1
        while (ni < nj-1):
            mid = (ni + nj)/2
            if matrix[mid][0]< target:
                ni = mid
            else:
                nj = mid
        if nj - ni == 1 and matrix[nj][0]<= target:
                ni = nj

        mi = 0
        mj = m-1
        while (mi < mj-1):
            mid = (mi + mj)/2
            if matrix[ni][mid] < target:
                mi = mid
            elif matrix[ni][mid] > target:
                mj = mid
            else:
                return True
        if mj - mi == 1 and (matrix[ni][mi] == target or matrix[ni][mi+1] == target):
            return True
        elif mj == mi and matrix[ni][mi] == target:
            return True
        else:
            return False