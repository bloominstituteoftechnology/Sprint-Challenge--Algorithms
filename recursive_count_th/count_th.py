'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) < 2: #guard word too small to contain "th"
        return 0
                
    if word[:2] == "th": # check first two letters
        return count_th(word[2:]) + 1 # increment count by 1
    else: # if "th" was not found
        return count_th(word[1:]) # advance

print(count_th("hellothth"))