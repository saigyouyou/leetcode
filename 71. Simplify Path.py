#-- coding:utf-8--
# 注意，这个方法只适用于绝对路径
class Solution(object):
    def simplifyPath(self, path):
        path = path.split("/")
        ret = []
        for i, j in enumerate(path):
            if j == '..':
                if len(ret)>0:
                    ret.pop()
            elif j != '.' and j!='':
                ret.append(j)
        return '/'+'/'.join(ret)