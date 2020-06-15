'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #keep track of the count
    str_count = 0
    
    #use .find to match 'th'
    occurance = word.find("th")
    
    # TBC - if not found or string is empty return 0
    if occurance == -1:
        return 0
    #if found, add one to the count
    else:
        str_count += 1
        return str_count
    
    #recursion here!
    str_count += count_th(word[occurance + 1: ])
    
    return str_count