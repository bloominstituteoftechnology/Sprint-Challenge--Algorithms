'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# U - we're looking for the characters t, followed by h, in case sensitive manner.
#     we need to count how many times we find the letters
#     we need to do it recursively, no loops

# P - the built in list method will separate the characters in 'word' and place them in a list
#     to accomplish this without loops we will need to use an if-else statement

# E
def count_th(word, counter=0): #Added a counter variable to the definition

    wordlist = list(word)   #This breaks the word into characters
    str1 = ""               #For joinging later
    
    if len(wordlist) <= 1:  #Empty word case
        return counter

    if wordlist[0:2] == ['t', 'h']:
        counter += 1
        
    newword = str1.join(wordlist[1:])   #Joins the wordlist, but leaves out the first letter
    
    return count_th(newword, counter=counter)   #Recursive return

# if __name__ == '__main__':
#     print(count_th('anthropopathism'))