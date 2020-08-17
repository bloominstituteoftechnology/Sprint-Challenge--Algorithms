import re

'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # keep track of count
    count = 0
    
    # create an array from the split word 
    splitWord = re.split('(th)', word)

    # get the length of that array
    length = len(splitWord)

    # 1. set base condition -> if the word passed in
    # 2. if the length is zero, stop

    if word == 'th':
        count+1
        length-1
    if length == 0:
        return    
    else:
        pass

    

    # return count of `th` occurences. case matters.
    return 


# def count_th(word):
#     # set base condition
#     if len(word) == 0:
#         return 0    

#     # return count of `th` occurences. case matters.
#     return word.count("th")

count_th('thTHthththTHHHHHHHTHTHHHT')