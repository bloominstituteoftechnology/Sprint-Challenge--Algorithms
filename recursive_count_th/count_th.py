'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    n = word.find("th")
    #if TH is not in word, return 0
    if n == -1:
        return 0
    #if TH is in word, will return until finished because of n + 2
    return 1 + count_th(word[n + 2:])

print(count_th("thetheisthebestthingthatthhasthinitithink")) #test
