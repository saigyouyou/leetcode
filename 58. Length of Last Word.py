class Solution(object):
	def lengthOfLastWord(self, s):
		s_list = s.split(' ')
		for i in range(len(s_list)-1, -1,-1):
			if len(s_list[i]) >0:
				return len(s_list[i])
		return 0