'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# def count_th(word):
#     # takes in word
#     # case matters
#     # need a variable to count 
#     # return a COUNT of how many occurences of "th" occur within word

#     # this is the better way, with the count method
#     # please see recursion utilization below
#     counter = word.count("th")
#     print(counter)
#     return counter

# count_th("thick Than thin")

def count_th(word):
    
    length1 = len(word) # get the length of the string
    length2 = len("th") # get the length of "th" = 2

    # Base Case
    if (length1 == 0 or length1 < length2): # if the length of the string is 0, or less than 2 ("th")
        return 0 # then the count is 0

    # Recursive Case
    if (word[0 : length2] == "th"): # if you start the word at the 0 index, and go to the 2 index, see if the letters == "th"
        return count_th(word[length2 - 1:]) + 1 # if they do, up the count by + 1, and keep going
    
    return count_th(word[length2 - 1:]) # otherwise, return the final count


count = count_th("thick Than thin")
print(count) # expected behavior = 2
count = count_th("thick than thin")
print(count) # expected behavior = 3
count = count_th("ththththt")
print(count) # expected behavior = 4