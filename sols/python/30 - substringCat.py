#
#
# Created By : Mitchell Van Swol
# Date : 5/8/2018
#

import sys

# find all starting indices of substrings in s that is a concatenation of 
# each word in words exactly once without any intervening characters

import collections

class Solution(object):
	def findSubstring(self, s, words):

		# check if there is bad input
		if not s or not words or not words[0]:
			return []

		word_len = len(words[0]) # all strings are the same length
		str_len = len(s) # length of input string
		num_words = len(words) # number of words
		word_set = set(words) # using hash implementation of set instead of 
		                      # list because its faster
		starting_points = []
		window = None
		counter = None

		def _check_word_fill_window(start):
			word = s[start:start + word_len]
			if word in word_set:
				counter[word] -= 1
				window.append(word)
			else:
				window.append(None)

		def _check_solution(start):
			(_, count) = counter.most_common(1)[0]
			if count == 0:
				starting_points.append(start)

		def _remove_word():
			word = window.popleft()
			if word:
				counter[word] += 1
			

		# check all possible solutoins which may not start at the beginning
		for i in range(word_len): 

			window = collections.deque()
			counter = collections.Counter(words)

			# populate counter, by checking words forward
			for j in range(i, i + num_words * word_len, word_len):
				_check_word_fill_window(j)

			_check_solution(i)

			# Check the words backwards to validate counter
			for k in range(i + word_len, (str_len + 1) - (word_len * num_words),
				           word_len):

				_remove_word()
				_check_word_fill_window(k + word_len * (num_words - 1))
				_check_solution(k)

		return starting_points


