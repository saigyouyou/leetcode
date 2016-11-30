#-- coding:utf-8--
#此处用了额外空间row+col
class Solution(object):
    def setZeroes(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        row = [1 for i in xrange(n)]
        col = [1 for i in xrange(m)]
        for i in xrange(n):
            for j in xrange(m):
                if matrix[i][j] == 0:
                    row[i] = 0
                    col[j] = 0
        for i in xrange(n):
            if row[i] == 0:
                for x in xrange(m):
                    matrix[i][x] = 0
        for j in xrange(m):
            if col[j] == 0:
                for y in xrange(n):
                    matrix[y][j] = 0

#实际上可以用第一行第一列作为标记，然后对0,0点特殊处理，使用额外的O(1)空间
class Solution(object):
    def setZeroes(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        extra = [1,1]
        for i in xrange(n):
            if matrix[i][0] == 0:
                extra[0] = 0
        for j in xrange(m):
            if matrix[0][j] == 0:
                extra[1] = 0
        for i in xrange(1,n):
            for j in xrange(1,m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in xrange(1,n):
            if matrix[i][0] == 0:
                for x in xrange(m):
                    matrix[i][x] = 0
        for j in xrange(1,m):
            if matrix[0][j] == 0:
                for y in xrange(n):
                    matrix[y][j] = 0
        if extra[0] == 0:
            for i in xrange(n):
                matrix[i][0] = 0
        if extra[1] == 0:
            for j in xrange(m):
                matrix[0][j] = 0