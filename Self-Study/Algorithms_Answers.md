```
a)  # O(n)
    a = 0   # O(1)
    # while a less than n^3
    # 0(n^3)
    while (a < n * n * n)
      # Increase a by 0n^2, 1n^2, 2n^2, 3n^2... and n^2
      a = a + n * n
```

n = 2
Stops when a = 8

1. 0+4
2. 4+4 = 8

n = 10
stops when a = 1000

1. 0+100
2. 100+100
3. 200+100
4. 300+100
5. 400+100
6. 500+100
7. 600+100
8. 700+100
9. 800+100
10. 900+100 = 1000

```
b)  O(1 + n * n * n * 8 * 1) or O(n^3)
    # O(1)
    sum = 0
    # runs n times O(n)
    for (i = 0; i < n; i++)
      # runs n - 1 times O(n - 1) or O(n)
      for (j = i + 1; j < n; j++)
        # runs n - 2 times O(n - 2) or O(n)
        for (k = j + 1; k < n; k++)
          # Constant O(8) or something around there doesn't matter much because constant
          for (l = k + 1; l < 10 + k; l++)
            # Constant O(1)
            sum++
```

```
c)  # O(n)
    bunnyEars = function(bunnies) {
      # Counting down for loop that runs n times O(n)
      if (bunnies == 0) return 0
      return 2 + bunnyEars(bunnies-1)
    }
```
