# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```
O(n) The result of the input increases as a constant of the input. 

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
O(n^2) The while loop functions like a for loop. There are two nested operations. The performance is the square of the input data.
```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

O(n) As a recursive function, input is subtracted by 1 and added with 2 uniformly. It is O(n) because the runtime will increase at a constant pace with the size of the input.

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

# psuedocode:
# for n number of floors
# find random floor between lowest and highest floor
# if n is less than f:
# n does not get broken. 
# else n gets broken
# if n is broken, find random floors again
# find f
# Complexity is O(log n) because this is a search problem
