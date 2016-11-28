# -- coding:utf-8 --
# 最简单的动态规划：将第一行第一列都置1，然后矩阵每一项为其左边和上边的项之和
class Solution(object):
    def uniquePaths(self, m, n):
        matrix = [[0 for i in xrange(n)] for i in xrange(m)]
        for i in xrange(n):
            matrix[0][i] = 1
        for i in xrange(m):
            matrix[i][0] = 1

        for i in xrange(1,m):
            for j in xrange(1,n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[m-1][n-1]