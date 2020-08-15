'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):

    charSearch = 'th'
    wordSize = len(charSearch)

    if wordSize > len(word):
        return 0

    if word[0:wordSize] == charSearch:
        return count_th(word[wordSize - 1:]) + 1

    return count_th(word[wordSize - 1:])

# def countSubstrig(str1, str2): 
      
#     n1 = len(str1); 
#     n2 = len(str2); 
      
#     # Base Case 
#     if (n1 == 0 or n1 < n2): 
#         return 0; 
  
#     # Recursive Case 
#     # Checking if the first 
#     # substring matches 
#     if (str1[0 : n2] == str2): 
#         return countSubstrig(str1[n2 - 1:], str2) + 1; 
  
#     # Otherwise, return the count  
#     # from the remaining index 
#     return countSubstrig(str1[n2 - 1:], str2); 
