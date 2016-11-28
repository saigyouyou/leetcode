# -- coding:utf-8 --
# 与Unique PathsI类似，可以新建一个矩阵，拿obstackeGrid作为障碍矩阵，也可以在obstackedGrid直接作为路径矩阵
# 此处采用了后者，将第一行第一列置为2，最后结果再除以2即可。
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        for i, j in enumerate(obstacleGrid):
            if j[0] == 1:
                break
            else:
                obstacleGrid[i][0] = 2
        for i,j in enumerate(obstacleGrid[0]):
            if j == 1:
                break
            else:
                obstacleGrid[0][i] = 2
        for ii, i  in enumerate(obstacleGrid):
            for jj, j in enumerate(i):
                if obstacleGrid[ii-1][jj] == 1:
                    a = 0
                else:
                    a = obstacleGrid[ii-1][jj]
                if obstacleGrid[ii][jj-1] == 1:
                    b = 0
                else:
                    b = obstacleGrid[ii][jj-1]
                if obstacleGrid[ii][jj] != 1 and ii>0 and jj>0:
                    obstacleGrid[ii][jj] = a + b
        return obstacleGrid[-1][-1]/2
