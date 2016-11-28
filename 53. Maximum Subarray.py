class Solution(object):
	def maxSubArray(self, nums):
		max_sum = 0
		max_sub = 0
		all_minus = True
		max_num = nums[0]
		n = len(nums)
		if n == 0:
			return 0
		elif n == 1:
			return nums[0]
		else:
			for i in nums:
				if i >max_num:
					max_num = i
				if i > 0:
					all_minus = False
				max_sub = max_sub + i
				if max_sub < 0:
					max_sub = 0
				if max_sub > max_sum:
					max_sum = max_sub
		return max_num if all_minus else max_sum
        