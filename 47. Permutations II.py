class Solution(object):
	def permuteUnique(self, nums):
		nums.sort()
		ret = []
		if len(nums) <= 1:
			ret.append(nums)
			return ret
		else:
			tmp = nums[0]
			for i,j in enumerate(nums):
				if i == 0 or (i > 0 and j > tmp):
					tmp = j
					for k in self.permuteUnique(nums[:i]+nums[i+1:]): 	
						ret.append(nums[i:i+1]+k)
					
			return ret