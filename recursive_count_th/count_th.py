'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    # We need to create a function that takes in a string
    # The function should check each neighbor element to determine 'th' groupings

    # First check length of the word
    if len(word) < 2:
        # if string is too small to containj the grouping 'th' return 0
        return 0

    # start by checking if first two elements contain 'th'
    if word[0] + word[1] == 'th':
        # return 1 added to the recursive run of the next two elements (increment index by 1)
        return 1 + count_th(word[1:])
    
    else:
        # if 'th' grouping wasn't found, run function again recursively using the next two elements
        return count_th(word[1:])

# test function
if __name__ == "__main__":
    word = 'taagsdhaklfjnhth;alafdgrjdthjgthd'
    print(count_th(word))
    word = 'lasdrfjkfljchjdsafkhderlkjhytgkhsgfshkalk'
    print(count_th(word))
    word = 't'
    print(count_th(word))
    word = 'thaffglk;fjdsgjef546dfgh45sdf362'
    print(count_th(word))