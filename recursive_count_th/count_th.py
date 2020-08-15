'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    target = 'th'
    word_len = len(word)
    count = 0
    word_ind=0
    end = word_len
    def find(word, target, count, word_ind):
        if len(word) == 0:
            return 0
    # if j+3 > word_len or word_len == 0:
    #     return count
    # # elif j+2 > word_len:
    # #     return count
    # elif word[i:j] == target:
    #     count =+ 1
    #     count_th(word[i+1:j+1])
    # else:
    #     count_th(word[i+1:j+1])
    # return count
        # if word[i:i+1] == 'th':
        #     count +=1
        #     i +=1
        # else:
        #     i+=1
    # return count
