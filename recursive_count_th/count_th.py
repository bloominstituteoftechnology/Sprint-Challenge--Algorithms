'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # 
    n = 0 #for counting the occurances of "th"
    position = word.find('th') #finds the location of "th" starting from "t"
    if position >= 0: #if the word has atleast 1 th then increments the count.
        n += 1
        word = word[position + 2:] #checks word's "th" location right after "h"' location
        n += count_th(word) #recursively calls the function and increase the counts of nth occurances if found one
    return n #returns the total occurances of "th"
