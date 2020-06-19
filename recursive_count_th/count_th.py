'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    s = list(word)
    count = 0 

    if len(s) <= 1:
        return count

    if s[0] != 't':
        s.remove(s[0])
        return count_th(''.join(s))
    else:
        if s[1] == 'h':
            count += 1
            s.remove(s[0])
            s.remove(s[0])
            if len(s) <= 1:
                return count
                
            else:
                return count + count_th(''.join(s))
        else:
            s.remove(s[0])
            return count_th(''.join(s))
    return count
    


