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


def whats_n1(n):
    a = 0
    count = 0
    while (a < n * n * n):
        count += 1
        a = a + n * n

    print("n1:10:", count)


def whats_n2(n):
    sum = 0
    counti = 0
    countj = 0
    for i in range(n):
        j = 1
        counti += 1
        while j < n:
            j *= 2
            sum += 1
            countj += 1
            print("j: ", j)
    print("n2:10:", counti, countj)


def bunnyEars(bunnies):
    if bunnies == 0:
        return 0
    print("ran")
    return 2 + bunnyEars(bunnies-1)


whats_n1(10)
whats_n2(10)
bunnyEars(10)


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
