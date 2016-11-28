#--coding:utf-8--
# a向后移动k个位置，然后让b指向head，之后ab同时向后移动直到a到达尾部，
# 然后裁切拼接链表即可。值得注意的是：
# 1. 要使用xrange而不是range，否则会出现memoryerror
# 2. 注意向后移动k个位置时假如移到了尾部，则记住链表长度，以k%length作为新的k重新移动一次。
class Solution(object):
    def rotateRight(self, head, k):
        if head == None or head.next == None:
            return head
        a = head
        count = 0
        end = False
        for i in xrange(k):
            a = a.next
            count = count+1
            if a == None:
                end = True
                break
        if end == True:
            k = k % count
            a = head
            for i in range(k):
                a = a.next
        b = head
        while (a.next != None):
            a = a.next
            b = b.next
        a.next = head
        head = b.next
        b.next = None
        return head