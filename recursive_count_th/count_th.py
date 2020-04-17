'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    ch = 'th'
    count = 0
    if len(word) < len(ch):
        return 0
    print(word)

    if (word == ch) | (word[0:2] == ch):
        return count+1

    return count_th(word[len(ch) - 1:])

# I'm close! I can get the character count from the first occurance or any other occurance but having trouble combining the counts


if __name__ == '__main__':
    print(count_th('theetheeeth'))