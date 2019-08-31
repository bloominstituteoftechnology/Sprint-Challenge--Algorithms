'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # sets count to 0 first
    count = 0

    # sets up the constant substring "th" to find
    substring = "th"

    # finds location of first substring and sets the first one
    index = word.find(substring)

    # if found sets index to 0 and increases count
    if index >=0:
        count += 1

        # then changes the word given to one not including the first found case
        word = word[index + len(substring):]

        # then recursivly calls the function to start again until the word is finished and no more "th" is found
        count += count_th(word)

    # then returns the count amount
    return count

    # if substring in word:
    #     print(True)
    # else:
    #     print(False)


# str = "there th"
# hello = "hello"
# surprisingly if no "th" is found then index is set to "-1" not sure why make sure to ask

# count_th(str)
#     # pass
    # TBC