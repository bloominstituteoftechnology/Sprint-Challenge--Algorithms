'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    if word[0] == 't':                   # if an instance of "t " shows up
        if word[1] == 'h':               # if t is present we want to check for "h "
            word[2:]                     # we count both "th" move to the rest of list
        else:
            word = word[1:]              # only a "t" was located so move forward
    count_th(word)                   
  
