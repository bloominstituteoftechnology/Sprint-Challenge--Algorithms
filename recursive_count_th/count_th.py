'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, sum=0):
    if "th" not in word:
        return sum

    if "th" in word:
        index = word.find("th")
        sum += 1
        return count_th(word[index + 2:], sum)
