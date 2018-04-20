#
#
# Created By : Mitchell Van Swol
# Date : 3/19/2018
#

import sys

# reverse groups of k nodes in a linked list
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        head_new = jump = ListNode(None)
        head_new.next = left = right = head

        while True:
        	count = 0
        	while right and count < k:
        		right = right.next
        		count = count + 1

        	# found a group of k nodes
        	# reverse and reconnect to outer list
        	if count == k:
        		prev, curr = right, left

        		for i in range(k):
        			curr.next, curr, prev = prev, curr.next, curr

        		#reconnect nodes to the master list
        		jump.next, jump, left = prev, left, right
        	else:
        		return head_new.next
        			



