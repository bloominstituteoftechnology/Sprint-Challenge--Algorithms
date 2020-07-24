'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) <= 1: # makes sure there is a string 
        return 0
    if word[0] + word[1] =='th': # checks for 'th' in the sting
        return 1 + count_th(word[1:]) # returns count of 'th's
    else:
        return count_th(word[1:]) 

print(count_th(""))
print(count_th("Not going to have any."))