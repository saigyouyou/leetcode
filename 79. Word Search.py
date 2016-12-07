# -- coding:utf-8--
# 一开始是使用矩阵存储已经走了的格子，走了的记为1.但是实际上发现由于python恼人的传递引用的问题
# 矩阵难以回溯，因此之后选择了使用一个栈来存储搜索的格点。
class Solution(object):
    def exist(self, board, word):
        def search(board, word):
            lw = len(word)
            [i,j] = stack[-1];
            if i+1 < mi and [i+1,j] not in stack and word[0] == board[i+1][j]:
                stack.append([i+1,j])
                if lw == 1 or search(board, word[1:]):
                    return True
                else:
                    stack.pop()
            if j+1< mj and [i,j+1] not in stack and word[0] == board[i][j+1]:
                stack.append([i,j+1])
                if lw == 1 or search(board, word[1:]):
                    return True
                else:
                    stack.pop()
            if j-1>= 0 and [i,j-1] not in stack and word[0] == board[i][j-1]:
                stack.append([i,j-1])
                if lw == 1 or search(board, word[1:]):
                    return True
                else:
                    stack.pop()
            if i-1>= 0 and [i-1,j] not in stack and word[0] == board[i-1][j]:
                stack.append([i-1,j])
                if lw == 1 or search(board, word[1:]):
                    return True
                else:
                    stack.pop()
            return False
#############################################
        if len(word) == 0:
            return True
        mi = len(board)
        if mi == 0:
            return False
        mj = len(board[0])
        if mj == 0:
            return False
        w = word[0]
        for i in range(mi):
            for j in range(mj):
                stack = []
                if board[i][j] == w:
                    stack.append([i,j])
                    if len(word)==1 or search(board, word[1:]):
                        return True
        return False