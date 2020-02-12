
'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count=0):
    print(f"The word is: {word}")
    if word[0:2] == "th":
        count += 1
        print(f"The count is: {count}")
        print(f"The word is: {word[2:len(word)]}")
        return count_th(word[2:len(word)], count)
    elif len(word[1:len(word)]) > 1:
        print(f"The count is: {count}")
        print(f"The word is: {word[1:len(word)]}")
        count = count_th(word[1:len(word)], count)

    return count

print(count_th("thethethe"))