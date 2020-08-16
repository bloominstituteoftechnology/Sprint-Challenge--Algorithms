'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #self.t = None
    #self.h = None
    count = 0  
    l = len(word)

    if l  == 0:
        return 0

    if word == "t":
        count = count + 1

    return count

word = "abcthefthghith"

print(count_th(word))