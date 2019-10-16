'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    if not word:
        return 0
    elif len(word) > 1 and word[0] == "t" and word[1] == "h":
        return 1 + count_th(word[1:])
    else:
        return 0 + count_th(word[1:])



# go through each element in word
# if element == t
# check if next element == h
#if true count + 1
# call count_th() on remaining elements in word.