'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    count = 0
    #this whole 0 thing is stupid
    return th(word,count)

def th(word,count):
    if word[0:2] == 'th':
        count += 1
    if word[2:] =='':
        return count
    return th(word[1:], count)   
  