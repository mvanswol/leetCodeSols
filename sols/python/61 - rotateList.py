#
#
# Created By : Mitchell Van Swol
# Date : 8/30/2018
#

# rotate a linked list by k places


class Solution(object):
	def rotateRight(self, head, k):

		if k == 0 or not head:
			return head

		length,node_list = self.get_length_and_nodes(head)


		new_k = k % length
		if new_k == 0:
			return head


		new_head = node_list[length - new_k]
		end_front = node_list[length - 1]
		node_list[length - new_k - 1].next = None
		end_front.next = head
		return new_head



	def get_length_and_nodes(self, head):

		temp = head
		length = 0
		node_list = []
		while temp is not None:
			node_list.append(temp)
			temp = temp.next
			length += 1


		return length, node_list