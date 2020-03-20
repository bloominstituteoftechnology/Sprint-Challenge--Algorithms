'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count=0):

    # Count kept resetting
    # I found the solution here: https://stackoverflow.com/questions/21965881/resetting-a-counter-after-recursion
    
    if len(word) <= 1:
        return count
    elif word[0:2] == "th":
        count += 1
        count = count + count_th(word[2:])
    else:
        count = count_th(word[1:])
    return count