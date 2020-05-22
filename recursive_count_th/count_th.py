'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    #Break Down problem into smaller fractions
    wdcheck = "th"
    wdcheck_count = len(wdcheck)
    word_count = len(word)

    #We should start with a base case

    if word_count < 2:
        return 0

    else:
        #check the first two letters from the word
        #python splice 
        if word[:2] == wdcheck:
            return 1 + count_th(word[2:])

        else:
            return count_th(word[1:])



    # if word_count == 0 or word_count < wdcheck_count:
    #     return 0

    # elif word[0: wdcheck_count] == wdcheck:
    #     #move toward base case
    #     return count_th(word[wdcheck_count - 1: ]) + 1
    # else:
    #     return count_th(word[wdcheck_count - 1: ])

