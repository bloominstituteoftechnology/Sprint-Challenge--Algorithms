# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:



```python
a)  a = 0 O(1)
    while (a < n * n * n): O(n*3) + 1
      a = a + n * n O(n*2) + O(1) + assignment 
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
count operations: I think there are 3 operations 



c)  def bunnyEars(bunnies): O(n)
      if bunnies == 0: O(1n)
        return 0

      return 2 + bunnyEars(bunnies-1) (2n)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.
