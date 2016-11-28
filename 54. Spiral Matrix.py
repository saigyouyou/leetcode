class Solution(object):
	def spiralOrder(self, matrix):
		ret = []
		i = 0
		j = 0
		mi = len(matrix)
		if mi == 0:
		    return []
		mj = len(matrix[0])
		while( i <= mi-1 and j <= mj-1 ):
			for m in range(j,mj):
				ret.append(matrix[i][m])
			i = i + 1
			for n in range(i,mi):
				ret.append(matrix[n][mj-1])
			mj = mj - 1
			if i <= mi-1:
				for m in range(mj-1, j-1, -1):
					ret.append(matrix[mi-1][m])
				mi = mi - 1
			if j <= mj-1:
				for n in range(mi-1, i-1, -1):
					ret.append(matrix[n][j])
				j = j + 1
		return ret
