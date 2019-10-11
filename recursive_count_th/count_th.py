'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    counter = 0
    if(len(word) < 2):
      return 0
    if word[-2] + word[-1] == "th":
        counter = counter + 1
    listW = list(word)
    listW.pop()
    return counter + count_th(listW)