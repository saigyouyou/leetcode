class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        b = []
        if len(nums) == 1:
            b.append(nums)
            return b
        else:
            for i,j in enumerate(nums):
                for k in self.permute(nums[:i]+nums[i+1:]):
                    b.append(nums[i:i+1]+k)
        return b
        
        