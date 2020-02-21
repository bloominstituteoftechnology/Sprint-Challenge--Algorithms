'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) < 2: #if length of word is less than two return 0
        return 0
    if word[0] == "t" and word[1] == "h": #if first letter is t and second letter is h
        return 1 + count_th(word[1:]) #add one for word with th in list
    else:
        return count_th(word[1:]) #or go through again

    print(count_th)


    pass
