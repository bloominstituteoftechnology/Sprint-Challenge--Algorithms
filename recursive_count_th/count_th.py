'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    def recu(new_word):
        index = new_word.find('th')
        if index != -1:
            nonlocal count
            count += 1
            if len(new_word) >= index + 4:
                spliced = new_word[index+2:]
                recu(spliced)
        else:
            return
        pass

    recu(word)
    
    # TBC

    # find first substring of th
    # add to count
    # pass back into function a new word spliced at the end of 'h'
    # if no 'th' found, return
    # end with returning the count

    return count