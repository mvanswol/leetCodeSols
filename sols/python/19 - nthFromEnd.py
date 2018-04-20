#
#
# Created By : Mitchell Van Swol
# Date : 2/28/2018
#

import sys


# given a list remove the nth element from the end

# solution : O(len(list))
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def removeNthFromEnd(self, head, n):
		fast = head
		slow = head

		for x in range(n):
			fast = fast.next

		if not fast:
			return head.next

		while fast.next:
			fast = fast.next
			slow = slow.next

		slow.next = slow.next.next
		return head
