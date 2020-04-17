'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''



def count_th(word):
    count = 1
    
    index = 1
    print(list(word[index-1]) + (list(word[index])))
    if count == 0:
        return 0
    if list(word[index-1]) == 'th':
        count +=1
        index =+ 1
        print(count)
        # count_th(word)
    else:
        count -=1 
        return 0
    # TBC
    
count_th("thanks")
# turn the word into a string
# recursion, itself, is a loop
# the function searches for index a and index b, iterating upward
# if index a is t and index b is h, and indexes a and b together are less than or equal to 1, pass, this is the base case
# if index a as 't' and index b as 'h' together are > 0, count+=1 and return to the count_th of the word
# might need to use a cache to track the first instance or second instance?

   
