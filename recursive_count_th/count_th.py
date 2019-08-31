'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# def count_th(word):
#     if word.count('th') < 1:
#         return 0
#     else:
#         return word.count('th')


def count_th(word):
    substring = "th"

    count = 0

    # set index to location of substring within string
    #   defaults to -1 if not found
    index = word.find(substring)
    if index >= 0:
        # increment count
        count += 1

        # slice string to start from the end of the previously found
        #   substring
        word = word[index + len(substring):]

        # increment count by recursively calling count_th
        count += count_th(word)
    return count


