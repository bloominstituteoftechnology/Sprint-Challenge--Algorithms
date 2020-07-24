# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```
# n=1 --> 1 iterations
# n=2 --> 2
# n=10 --> 10 

# O(n) linear increase with every step, since the algorithm iterations reflect n directly.


```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
# for inputs n=1 -->0, n=5 --> 15, n = 10 -->40, n=20 -->100 iterations. Follows a nlogn curve.

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0
    
      return 2 + bunnyEars(bunnies-1)
```
# O(1) always returns None, misses else: statement which would be O(n) 


## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

<!-- Assuming the floors are a presorted list (0,1,2,3, etc.) I would take a binary search approach.
1. drop an egg at the n/2 th floor, and note the result. 
   1. If the egg broke, we eliminate all higher floors as points of interest because of the properties of f.
   2. If the egg did not break, we eliminate all lower floors as points of interest.
2. Each time we drop an egg we do so from the middle of the range in which we have interest.
   1. This means that on average we eliminate possible answers very quickly.
   2. The time complexity of this approach would be O(logn) where n is the amount of floors, the larger the building, the more floors we need to consider. -->