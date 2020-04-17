'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
	word_size = len(word)
	th_count = 0

	def count_helper(wrd):
		if len(wrd) < 2:
			return
		else:
			if wrd[0] == 't' and wrd[1] == 'h':
				nonlocal th_count 
				th_count += 1
			if len(wrd) == 2:
				return
			else:
				count_helper(wrd[1:])

	count_helper(word)

	return th_count