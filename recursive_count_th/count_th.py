'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # game plan:
    # if find occurrence of 'th' in word, slice after occurrence, recurse with remainder of string
    # returns 1 + recursive function w/ sliced string
    # base case 'th' not found, return 0

    # TBC

    if 'th' in word:
        i+2 = word.find('th')                     # the index of the first occurrence of 'th' plus 2
        return 1 + count_th(word[i:])             # recurse with slice of string starting after 'th'

    else:
        return 0                                  # otherwise if no 'th', return 0

# print(count_th("the cat that sits on the thatch basket"))