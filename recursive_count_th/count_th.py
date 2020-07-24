'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0

    if len(word) <= 1:
        return 0
    if (word[0] + word[1] == 'th'):
        count += 1
        word[1:]
    elif word[1] == 't':
        word[1:]
    else:
        word[2:]
    return count + count_th(word[1:])


"""
Plan:  
Keep count of 'th' occurances in string by setting 'count = 0'
Base Case: str <= 1 return 0
else if the first 2 letters == 'th' increment count by 1
else if they don't match, check if the next letter is t and then slice.
else slice the first 2 letters
else return not found ---> Not sure if I did this? 

"""