'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
	if len(word) < 2:
		return 0
	elif word[:2] == "th": # found th, next run skip the next two letters
		return count_th(word[2:]) + 1
	else: # try again without first letter
		return count_th(word[1:])


print(count_th("thesarusth"))