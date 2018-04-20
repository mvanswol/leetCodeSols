#
#
# Created By : Mitchell Van Swol
# Date : 3/19/2018
#

import sys


# swap pairs of nodes in a linked list

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def swapPairs(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if not head or not head.next:
			return head

		temp = head.next
		head.next = self.swapPairs(temp.next)
		temp.next = head
		return temp