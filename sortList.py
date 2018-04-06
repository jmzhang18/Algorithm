# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if (head == None):
        	return head
        if (head.next==None):
        	return head

        pre = head
        p1 = head
        p2 = head

        while (p2!=None and p2.next!=None):
        	pre = p1
        	p1 = p1.next
        	p2 = p2.next.next

        pre.next = None
        l1 = sortList(head)
        l2 = sortList(p1)

        return self.__merge(l1, l2)

    def __merge(self, l1, l2):
    	l = ListNode(0)
    	p = l

    	while (l1!=None and l2!=None):
    		if (l1.val < l2.val):
    			p.next = l1
    			l1 = l1.next
    		else:
    			p.next = l2
    			l2 = l2.next
    		p = p.next

    	while (l1!=None):
    		p.next = l1
    		l1 = l1.next
    		p = p.next

    	while (l2!=None):
    		p.next = l2
    		l2 = l2.next
    		p = p.next

    	return l.next