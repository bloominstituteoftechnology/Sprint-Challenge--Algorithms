'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    
    # TBC
    i = word.find("th") #Find first orruance of "th" in word
    if i == -1: #if it does not occur, then there are no more "th" in rest of word. Return 0
        return 0

    # We have found first occurance of "th" starting at index i. So we have 1
    # So now call this function again with rest of word starting from i + 2 (length of "th")
    return 1 + count_th(word[i+2:])

print(count_th("abcthefthghith"))


