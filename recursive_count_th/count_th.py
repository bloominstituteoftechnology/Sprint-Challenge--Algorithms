'''

Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# Your function should take in a single parameter (a string `word`)
def count_th(word):
    
    # TBC
    
    #start 
    count = 0
    #base any word 
    # string index
    if len(word) < 2:
        return count
    letters = word[0] + word[1] # get the two letters combined
    
    if letters == "th": # if letters are th then put them in the count 
        count += 1
        
    count += count_th(word[1:])
    return count
    
    
    
