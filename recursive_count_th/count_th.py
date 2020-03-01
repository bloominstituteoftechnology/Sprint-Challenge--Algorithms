'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    count = 0
    if len(word) <= 1:
        return 0
    if word[0:2] == "th":
        count += 1
        print(word)
        print(1)
        return count + count_th(word[1:])

    return count_th(word[1:])


# count_th("abcthxyz")
print(count_th("THtHThth"))


""" 
old code: 

if word == "th":
        return word

    if word[0].lower() != "t" and word[1].lower() != "h":
        print(word)
        return count_th(word[2] + word[2:])
    elif word[len(word)-2].lower() != "t" or word[len(word)-1].lower() != "h":
        print(f"elif: {word[:len(word)-1]}")
        return count_th(word[:len(word)-1])


 """
