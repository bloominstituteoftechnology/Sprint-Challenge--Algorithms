'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    if word == "":
        return 0
    else:
        start_index = word.find('th')
        end_index = start_index + 2
        print(f"{start_index} until {end_index}")
        if word[start_index:end_index].islower() and "th" in word[start_index:end_index]:
            count += 1
            print(f"Current count = {count}")
            print(f"Cut Happened: {word[start_index:end_index]}")

    return count + count_th(word[end_index:])



print(count_th("abcthxyz"))