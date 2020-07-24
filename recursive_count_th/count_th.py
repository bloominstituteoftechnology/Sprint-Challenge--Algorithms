'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #if the word is less than 2 characters, it cannot contain th, therefore will return 0    
    if len(word)<2:
        return 0
    if word[:2] == 'th': #if first 2 chars are 'th'
        return count_th(word[1:]) +1 #run again, starting from the next char, and add 1 to document the 'th' found

    return count_th(word[1:]) #basically keeps the recursion going even when a 'th' isnt found, until there are less than 2 chars left to check

print(count_th('abcthxythz')) 
# for my own pratice, would this big O then be O(n)? Since it needs to loop through every element in order to complete basically?
