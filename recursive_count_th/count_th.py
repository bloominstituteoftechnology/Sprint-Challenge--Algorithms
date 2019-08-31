'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    word_length = len(word)
    if word_length == 0 or word_length < 2:
        return 0
    elif word[0:2] == "th":
        return count_th(word[1::]) + 1
    else:
        return count_th(word[1::])
 
word_one = "abcthxyz"
word_two = "thhtthht"

count_th(word_one)
count_th(word_two)
