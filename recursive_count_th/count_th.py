'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    total = 0

    if len(word) <= 0:
        return 0

    def count(str, point=1):
        nonlocal total
        if len(str) == point:
            return total
        if str[point - 1] + str[point] == "th":
            total += 1
        point += 1
        return count(str, point)

    return count(word)
