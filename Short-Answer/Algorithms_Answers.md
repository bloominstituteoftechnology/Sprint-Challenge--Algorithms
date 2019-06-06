Add your answers to the Algorithms exercises here.# Analysis of Algorithms

## Exercise I

```
a)  a = 0 #constant O(1)
    while (a < n * n * n): #linear O(N)
      a = a + n * n 

    O(1) + O(N) ...drop lower order
```
        ANSWER: O(N)

```
b)  sum = 0 #constant #O(1) ... ignore
    for i in range(n): #O(N) 
      i += 1
      for j in range(i + 1, n): #O(N)
        j += 1
        for k in range(j + 1, n): #O(N)
          k += 1
          for l in range(k + 1, 10 + k): #O(1) .... not dependant on n
            l += 1
            sum += 1

        O(N) x O(N) x O(N) x O(1) = O(N^3)
```
        ANSWER: O(N^3)

```
c)  def bunnyEars(bunnies):
      if bunnies == 0: O(1) .... ignore
        return 0

      return 2 + bunnyEars(bunnies-1) #O(N)
```

        ANSWER: O(N)

## Exercise II
```
Suppose that you have an _n_-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get broken if dropped off a floor less than floor _f_. Devise a strategy to determine the value of _f_ such that the number of dropped eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode and give the runtime complexity of your solution.
```

ANSWER:

high_broken = true
low_broken = false
low = 0
high = n


While low_broken != high_broken:
    high_broken = throw(high)       #O(N)
    low_broken = throw(low)         #O(N)
    f = low                         #O(1)
    low += 1                        #O(1)
    high -= 1                       #O(1)
return f


Time complexity: O(2^n)
