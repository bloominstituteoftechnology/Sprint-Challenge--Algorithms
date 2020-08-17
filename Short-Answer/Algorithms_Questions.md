# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```


```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

1) start from the middle floor f = n//2, 
2) drop a egg
3) check if the egg is broken or not
4) if egg is  broken repeat  the same process for the left subarray of   n//2(0 to f-1)
5) if egg is not broken repeat the process for  the right subarray of   n//2(f+1, n)
6) Repeat step 1 to 5 until n = 0 or n= n

Runtime complexity for this solution will be O(logn) 
