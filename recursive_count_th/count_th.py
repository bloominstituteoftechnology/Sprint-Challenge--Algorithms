'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
	n = 0
	count = 0
	if len(word) <= 1:
		return 0
	if word[n:n+2] == "th":
		count = 1 + count_th(word[n+1:])
	if word[n:n+2] != "th":
		count = count_th(word[n+1:])
	return count