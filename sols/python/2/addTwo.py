#
#
# Created By : Mitchell Van Swol
# Date : 1/23/2018
#

import sys

# Given a two linked lists, and them together 

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


# Add two linked lists together
# solution in O(max(len(l1), len(l2)))
def addTwoNumbers(l1, l2):
	head = None
	prev = None
	temp = None

	carry = 0
	while(l1 is not None or l2 is not None):
		# read input
		l1_val = 0 if l1 is None else l1.val
		l2_val = 0 if l2 is None else l2.val

		total = l1_val + l2_val + carry

		if total >= 10:
			carry = 1
			total = total - 10
		else:
			carry = 0

		temp = ListNode(total)

		if not head:
			head = temp
		else:
			prev.next = temp

		prev = temp

		l1 = None if l1 is None else l1.next
		l2 = None if l2 is None else l2.next

	if carry:
		temp = ListNode(carry)
		prev.next = temp

	return head




def printList(head):

	node = head
	output = ""
	while node:
		output += str(node.val) + " -> "
		node = node.next
	print(output)

def createList(inputList):

	head = None
	temp = None
	prev = None
	for num in inputList:
		temp = ListNode(num)

		if not head:
			head = temp
		else:
			prev.next = temp

		prev = temp

	return head

input_file = open(sys.argv[1])
list_one_head = createList([int(x) for x in input_file.readline().split()])
printList(list_one_head)
list_two_head = createList([int(x) for x in input_file.readline().split()])
printList(list_two_head)
printList(addTwoNumbers(list_one_head, list_two_head))
