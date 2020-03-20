def count_th(word):
	word_size = len(word)
	th_count = 0

	def count_helper(wrd):
		if len(wrd) <= 1:
			return
		else:
			if wrd[0] == 't' and wrd[1] == 'h':
				nonlocal th_count 
				th_count += 1
			if len(wrd) == 2:
				return
			else:
				count_helper(wrd[2:])

	count_helper(word)

	return th_count


print(count_th("wothdth"))
