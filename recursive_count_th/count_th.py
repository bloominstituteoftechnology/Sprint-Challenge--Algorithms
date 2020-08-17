'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    n1 = len(word)
    n2 = len('th')  
    
    term = 'th'
    # Base Case 
    if (n1 == 0 or n1 < n2): 
        return 0; 
    # Recursive Case 
    # Checking if the first 
    # substring matches 
    if (word[0 : n2] == term): 
        return count_th(word[n2 - 1:]) + 1; 
  
    # Otherwise, return the count  
    # from the remaining index 
    return count_th(word[n2 - 1:]); 


    
