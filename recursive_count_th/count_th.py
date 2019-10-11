'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    if len(word) < 2: #impossible, so return 0
        return 0
    if word[:2] == 'th': #letters 'th' exist as the first 2 letters in the string, we then add 1 to our counter and continue to check for more occurances
        return 1 + count_th(word[2:])
    else: #first 2 letters do not match 'th' so we run the function again to continue checking the rest of the string
        return 0 + count_th(word[1:])