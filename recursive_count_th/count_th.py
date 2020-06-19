'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count=0, start=0, end=2):
    if end > len(word):
      return count
    if word[start: end] == "th":
      count += 1
      start += 1
      end += 1
      return count_th(word, count, start, end)
    if word[start: end] != "th":
      start += 1
      end += 1
      return count_th(word, count, start, end)
    return count
    
