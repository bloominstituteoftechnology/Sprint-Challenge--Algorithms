'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # see if list has more that 2 elements. If not, return None
    count = 0
    #  splitWord = split(word) # spliting the word list

    if len(word) <= 1:
        return count

    # start a count list to hold the occurences of th

    # pointer = 0

    # if the first letter in "word" is "t", check if next element is "h"
    elif word[0] == 't' and word[1] == 'h':
        # add to count
        count += 1
        # increment the list (or remove 1st item)
        # word.pop(0)

    # reset count to start at the next element in the list
    # count = count + count_th(word[1:])

    # return count
        return count + count_th(word[2:])
    
    else:
        return count_th(word[1:])

    # #self.t = None
    # #self.h = None
    # count = 0  
    # l = len(word)

    # if l  == 0:
    #     return 0

    # if word == "t":
    #     count = count + 1

    # return count

word = "abcthefthghith"

print(count_th(word))