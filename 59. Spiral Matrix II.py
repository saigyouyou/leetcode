class Solution(object):
	def generateMatrix(self, n):
		ret = [[0 for i in range(n)] for i in range(n)]
		i = 0
		j = 0
		mi = n
		mj = n
		c = 1
		while( i <= mi-1 and j <= mj-1 ):
			for m in range(j,mj):
				ret[i][m] = c
				c = c + 1
			i = i + 1
			for n in range(i,mi):
				ret[n][mj-1] = c
				c = c + 1
			mj = mj - 1
			if i <= mi-1:
				for m in range(mj-1, j-1, -1):
					ret[mi-1][m] = c
					c = c + 1
				mi = mi - 1
			if j <= mj-1:
				for n in range(mi-1, i-1, -1):
					ret[n][j] = c
					c = c + 1
				j = j + 1
		return ret