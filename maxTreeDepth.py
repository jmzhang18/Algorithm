#!/usr/bin/env python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def maxDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		def depthSearch(node, current_level):
			if (node==None):
				return current_level
			left_depth = current_level
			right_depth = current_level
			if (node.left != None):
				left_depth = depthSearch(node.left, current_level+1)
			if (node.right != None):
				right_depth = depthSearch(node.right, current_level+1)
			current_depth = max(left_depth, right_depth)
			print("depth: ", current_depth)
			return current_depth

		if (root==None):
			return 0
		else:
			return depthSearch(root, 1)



