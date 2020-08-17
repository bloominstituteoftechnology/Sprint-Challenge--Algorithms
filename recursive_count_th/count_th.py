'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # TBC
    l = len(word) #* l is equal to the length of word
    if l == 0: #* if l is equal to zero
        return 0 #* return zero

    elif word[:2] == "th": #* if the first two letters are "th"
        return 1 + count_th(word[2:]) #* return 1 plus the rest of the word to keep moving

    else:
        return count_th(word[1:]) #* if not 'th' return the rest of the word

#* ALL TESTS PASSED