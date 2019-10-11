'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    counter = 0

    # What is the base case?
        # len(word) <= 2 & word does not include 'th'
        # Then we should return

    # Since we have to count something, might it be prudent to add a counter outside of a recursive helper function?

    # IDEA
    # Check if word[0:2] are 'th'
        # If so, add 1 to counter
    
    # Then recursively call the function count_th with word[2:]
    
    pass

print("the"[2:])