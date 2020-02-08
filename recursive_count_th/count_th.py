'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    # start the problem by indentifying the occurance of 'th' in the word using word.find 
    i = word.find("th")
    if i == -1:
        return 0 # if there is no "th" occuring in the code, 0 will be returned 
    # if there is a "th" occuring, the function will be called again and again til the end of the snetence to find out how many "th" there actually are.
    return 1 + count_th(word[i +2:])

    print(count_th("theresfeatherinmyleatherweather"))