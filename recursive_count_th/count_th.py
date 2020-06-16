'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.

need to return a count so I could use a  variable that starts at 0 and increases 
try access the letters by index so that t would be first[0] and h would be second[1]

'''

def count_th(word):
    increment = 0 
    #Create base case, if length of word is 1 or less, stop it 
    if len(word) <= 1:
        return 0
    else:
        #use the index letters here 
        if word[0] == 't' and word[1] == 'h':
            
            # print(word)
            # print('first letter', word[0])
            # print('last letter', word[1])
            increment = increment + 1 
            #start at the beginning of the string and continue through, need counter because it can't move through word without it
    return count_th(word[1:]) + increment 

print('0', count_th('')) 
print('1',count_th('abcthxyz'))
print('3', count_th('abcthefthghith')) 
print('2', count_th('thhtthht'))  
print('1', count_th('THtHThth')) 