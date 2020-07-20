'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if word == "":
        return 0
    if word[0] == "t" and word[1] == "h":
        return 1 + count_th(word[1:])
    if word[-1] == "t" and word[-2] == "h":
        return 1 + count_th(word[:1])
    else:
        return count_th(word[1:])


#print(count_th(none))