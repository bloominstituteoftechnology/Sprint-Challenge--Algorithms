'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    length = len(word)

    if length >= 3 and word[1:3] == "th":
        return 1 + count_th(word[3:])
    elif length >= 2 and word[:2] == "th":
        return 1 + count_th(word[2:])
    elif length >= 2:
        return count_th(word[2:])
    else:
        return 0

print(count_th("word"))
print(count_th("wings and things"))
print(count_th("ThthThthTh"))
