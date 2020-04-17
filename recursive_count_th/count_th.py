'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # TBC
    # start the algorithm by identifying the occurance of "th" in word using word.find
    i = word.find("th")
    if i == -1:
        return 0  # if there is no th occurring within the code, then return 0 because there is no th
    # If there is an occurance of th found within the word, the function will be called again and the rest of the word will pass through because we are adding i+2 meaning looking past
    # the length of the previous th and looking for some more thhhhhhhhhhhhhhhh
    return 1 + count_th(word[i + 2:])


print(count_th("theressomefeatherinmyleatherweather"))
# this should count 4 different occurances of "th"
