class Solution(object):
	def groupAnagrams(self, strs):
		tmp = {}
		for i in strs:
			si = ''.join(sorted(i))
			if si in tmp:
				tmp[si].append(i)
			else:
				tmp[si] = [i]
		ret = []
		for i in tmp:
			ret.append(tmp[i])
		return ret
        