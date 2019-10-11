'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, count=0):
    #check if the length is less than wo
    if len(word) < 2:
        return 0
    #check if the first letter is t and second letter is h
    #remove the first two letters and increase the count
    elif word[0:2] == 'th':
        return 1+count_th(word[2:])
    #remove the first letter
    else:
        return count_th(word[1:])

        

print(count_th('thee'))
