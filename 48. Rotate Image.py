class Solution(object):
    def rotate(self, matrix):
        matrix.reverse()
        x = len(matrix)
        for i in xrange(1,x):
        	for j in xrange(0,i):
        		matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]