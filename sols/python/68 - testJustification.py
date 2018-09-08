#
#
# Created By : Mitchell Van Swol
# Date : 9/7/2018
#

# text justification
class Solution(object):
	def fullJustify(self, words, maxWidth):

		result = []
		num_words = len(words)
		curr_words = [words[0]]
		curr_len = len(words[0])

		for idx, word in enumerate(words[1:], 1):
			if curr_len + 1 + len(word) <= maxWidth:
				curr_words.append(word)
				curr_len = curr_len + 1 + len(word)

			else:
				temp_str = ''.join(curr_words)
				curr_num_words = len(curr_words)

				if curr_num_words == 1:
					result.append(temp_str + " "*(maxWidth - len(temp_str)))
				else:
					spaces_remaining = maxWidth - len(temp_str)
					fill, remain = divmod(spaces_remaining, curr_num_words - 1)
					temp_str = curr_words[0]
					for i in range(1, curr_num_words):
						if remain >= i:
							temp_str += ' ' *(fill + 1) + curr_words[i]
						else:
							temp_str += ' '*fill + curr_words[i]

					result.append(temp_str)
				curr_words = [word]
				curr_len = len(word)


		if curr_len > 0:
			temp_str = ' '.join(curr_words)
			result.append(temp_str + ' '*(maxWidth - len(temp_str)))

		return result

