# -- coding:utf-8 --
# 类似62, 只不过计算值的时候是本单元值加上左边和上面两个中比较小的那个
class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        matrix = [[0 for i in xrange(n)] for i in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 and j == 0:
                    matrix[i][j] = grid[i][j]
                elif i == 0:
                    matrix[i][j] = grid[i][j] + matrix[i][j-1]
                elif j == 0:
                    matrix[i][j] = grid[i][j] + matrix[i-1][j]
                else:
                    matrix[i][j] = grid[i][j]+ min(matrix[i-1][j],matrix[i][j-1])
        return matrix[m-1][n-1]