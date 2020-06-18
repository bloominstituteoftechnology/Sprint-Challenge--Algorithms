'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
#  set the initial count:
    count = 0

#  Set up the base cases
#  Length of word less than 2:
    if len(word) < 2:
        return count

# The word is 'th'
    if word[0: len("th")] == "th":
        count = 1 + count_th(word[1:])
        return count

# Length of word is greater than 2,
    else:
        count = count_th(word[1:])
        return count
  
        
print(count_th(""))
print(count_th("abcthxyz"))
print(count_th("abcthefthghith"))
print(count_th("thhtthht"))
print(count_th("THtHThth"))
print(count_th("Now is the time for all good men to come to the aid of their country"))
