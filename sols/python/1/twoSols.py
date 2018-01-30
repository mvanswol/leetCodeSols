#
#
# Created By : Mitchell Van Swol
# Date : 1/23/2018
#

# Given a list, see if any two elements in the list add up to a given sum

import sys

# Inital idea is to brute force with nested for loops
# this is a O(n^2) but we can probably do better

# store the values in a map with the value as a key and 
# the index as the value 
# loop over each key and see if target - key is present
# if so then that is the solutions
# note : we need to check that we didn't use the same value twice
def twoSum(nums, target):

	value_map = {}
	for value, key in enumerate(nums):
		if key in value_map:
			value_map[key].append(value)
		else:
			value_map[key] = [value]

	for key in value_map:
		print(value_map[key])
		if (target - key) in value_map:
			if (target - key) != key:
				return [value_map[key][0], value_map[target - key][0]]
			else:
				return [value_map[key][0], value_map[key][1]]
	return [-1, -1]


input_file = open(sys.argv[1])
input_list = [int(i) for i in input_file.readline().split()]
target = int(input_file.readline())
input_file.close()

print(twoSum(input_list, target))





