'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


# MARK - Solution runs in 0(n) time #

def count_th(word):
	
    # check the last two letters
    #if they are the value we're looking for, remove them and return count_th + 1
    #if the last two letters are not the value we're looking for, remove them and return count_th
    #Else, remove only the last letters left 

    if len(word) <= 1:

        return 0

    elif word[-2:] == "th":

        return count_th(word[:-2]) + 1

    elif word[-2] != "h": 

        return count_th(word[:-2])

    else:

        return count_th(word[:-1]) # otherwise, just remove the last letter, so we can check again for "th"



   
