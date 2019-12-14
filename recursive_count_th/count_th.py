'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
count = 0

def count_th(word):
    global count

    def counter(count):
        return count + 1

    # base 
    if len(word) < 2:
        return 0
    
    # recursion !!!
    if(word[0:2] == 'th'):
        return count_th(word[2 - 1:]) + counter(count) # add to counter if found
    
    return count_th(word[2 - 1:])    # advance to next pair
    
    # pass

# str = "tthTH"
str = ""
# str = "abcthxyz"
# str = "abcthefthghith"
# str = "thhtthht"
# str = "THtHThth"

print(count_th(str))