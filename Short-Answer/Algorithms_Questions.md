# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

This function runs in O(n) time (or "linear time"), 
where n is the number of items a is less than n * n * n. If a is less than n * n * n 10 times, 
we have to do a = a + n * n 10 times. If it's less 1000 items, we have to continue 1000 times.


```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

O(n^2)

Here we're nesting two loops. 
If our array has n items, our outer loop runs n times and our inner loop runs n times 
for each iteration of the outer loop. Thus this function runs in O(n2) time (or "quadratic time"). 

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

0(n)

We iterate through the number of bunnies



## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.


````
start at middle of the building, drop egg, if egg does not break, you can eliminate all of the buildings below,
if egg breaks, you can eliminate all of the buidlings above. Continue to do this until f is found

O(logn)

