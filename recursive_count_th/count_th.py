'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    #base case
    count = 0 # sets count to 0 to start
    th_occurences = "th" # setting up to find the occurences of "th" 
    
    indx = word.find(th_occurences) #set up index to find the "th" occurances
    
    #if "th" is found set to 0 and increase count
    if indx >=0:
        count +=1 # increase count by 1
        
        word = word[indx + len(th_occurences):] #changes word to next given/not including first case

        count += count_th(word) # recursively starts func until word is finished 
        # and no more "th" is found

    return count #return count







 









    #pass
