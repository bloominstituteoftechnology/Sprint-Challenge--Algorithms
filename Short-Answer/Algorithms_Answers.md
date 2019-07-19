1(a)The first line is of O(1), the second line is O(n) and the third line is O(1)

Making the worst case time complexity O(n)

1(b)
b)  sum = 0                              O(1)
    for i in range(n):                   O(n)
      i += 1                             O(1)
      for j in range(i + 1, n):          O(n)
        j += 1                           O(1)
        for k in range(j + 1, n):        O(n)
          k += 1                         O(1)
          for l in range(k + 1, 10 + k): O(1)
            l += 1                       O(1)
            sum += 1                     O(1)

Making the worst case time complexity O(n^3)


1(c)the only n complexity is in the last line, aking the final worst case complexity O(n)

2-I would start at the middle floor to see if the egg broke, and if so, I would go to the top, if not I would go between the bottom and the middle, and I would just keep cutting the distance in half up or down, this reduces the complexity to O(logn) complexity. 
