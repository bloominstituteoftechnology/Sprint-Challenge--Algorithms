'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # if the length of the word is less than 2:
    if len(word) < 2:
        # return 0
        return 0
    # if the word contains t or h
    if word[0] == 't' and word[1] == 'h':
        # return count of 1 + count of 'th' sliced
        return 1 + count_th(word[2:])
    else:
        # else return through word
        return count_th(word[1:])
    pass

print(count_th("health"))
print(count_th("fairy"))
print(count_th("thanks"))
print(count_th("theatherth"))