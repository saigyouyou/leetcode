class Solution(object):
	def canJump(self, nums):
		n = len(nums)
		max_i = 0
		if n == 1:
			return True
		for i, j  in enumerate(nums):
			tmp_i = i + j
			if i > max_i:
				return False
			elif max_i < tmp_i:
				max_i = tmp_i
			if max_i >= n-1:
				return True

		if max_i >= n-1:
			return True
		else:
			return False