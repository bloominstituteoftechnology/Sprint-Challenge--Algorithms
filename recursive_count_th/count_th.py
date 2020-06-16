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
        count = 0

# Length of word is 2 AND the word is "th":
    elif len(word) == 2:
        if word == "th":
            count = count + 1

# Length of word is greater than 2,
# use String.count() method on the main string 
# with sub-string, 'th', passed as argument.
    else:
        return count + count_th(word[1:])
  
        

print(count_th(""))
print(count_th("abcthxyz"))
print(count_th("abcthefthghith"))
print(count_th("thhtthht"))
print(count_th("THtHThth"))
print(count_th("Now is the time for all good men to come to the aid of their country"))
