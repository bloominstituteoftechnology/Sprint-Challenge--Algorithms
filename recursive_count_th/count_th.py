'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    def count_th_helper(word, counter):
        # len(word) <= 2, the word does not include 'th'
        if len(word) < 2:
            return counter

        # Check if word[0:2] are 'th'
        if word[0:2] == 'th':
            # If so, add 1 to counter
            counter += 1
    
        # Then recursively call the function count_th with word[1:]
        # Move up one letter and check if [0:2] are 'th'.
            # If we care about performance, we could check if word[1] == 't'.
            # If so, we could move over 1, else 2
        return count_th_helper(word[1:], counter)




    return count_th_helper(word, 0)

# print(count_th("thetHth"))