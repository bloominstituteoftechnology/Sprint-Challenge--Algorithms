'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
total = 0
next = 0
def count_th(word):
    # TBC
    global next
    global total
    if next == 0:
        total = 0
    if word.find('th') == -1:
        return 0
    next = word.find('th',next) +1
    if next == 0:
        return total
    total +=1
    if next >= len(word):
        next = 0
        return total
    count_th(word)
    return total 

    