#
#
# Created By : Mitchell Van Swol
# Date : 3/19/2018
#

import sys
import heapq


# merge two sorted lists

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

#utilize a heap for more efficient solution
#this eliminates the number of comparasions necessary
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        heap = []

        for node_list in lists:
            curr_node = node_list
            while curr_node != None:
                val = curr_node.val
                #print(val)
                heapq.heappush(heap, curr_node.val)
                curr_node = curr_node.next


        head = curr = ListNode(None)

        for i in range(len(heap)):
            val = heapq.heappop(heap)
            #print(val)
            curr.next = ListNode(val)
            curr = curr.next


        return head.next



