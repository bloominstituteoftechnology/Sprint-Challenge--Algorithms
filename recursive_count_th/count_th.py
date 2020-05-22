'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# if the length of word is less than 2 return 0
# if the ending of word is equal to "th" return 1
# and if the following 2 letters are "th" return 1 + the count of words
def count_th(word):
    # base case
    if len(word) < 2:
        return 0
    
    # TBC
    elif word[0:2] == 'th':
        return 1 + count_th(word[2:])
    else:
        return count_th(word[1:])
    

print(count_th("awesomeness"))
print(count_th("twentieth"))
print(count_th("throw"))
print(count_th("theeth"))