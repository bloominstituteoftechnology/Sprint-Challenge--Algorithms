'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # #self.t = None
    # #self.h = None
    # count = 0  
    # l = len(word)

    # if l  == 0:
    #     return 0

    # if word == "t":
    #     count = count + 1

    # return count


    # see if list has more that 2 elements. If not, return None
    if (len(word) < 2):
        return None

    # start a count list to hold the occurences of th
    count = 0

    # if the first letter in "word" is "t", check if next element is "h"
    if word[0] == 't' and word[1] == 'w':
        # add to count
        count += 1

    # reset count to start at the next element in the list
    count = count + count_th(word[1:])

    # return count
    return count



word = "abcthefthghith"

print(count_th(word))