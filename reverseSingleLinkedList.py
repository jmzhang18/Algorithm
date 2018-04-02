#!/usr/bin/env python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def reverseRecursion(self, node, prev=None):
		if (node==None):
			return prev
		tmp = node.next
		node.next = prev
		prev = node
		node = tmp
		return self.reverseRecursion(node, prev)
	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		return self.reverseRecursion(head)


