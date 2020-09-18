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

floor = f
eggs = e
building.mid = number of floors

if floor is at a level where the eggs get broken
then the eggs dropped from that level are infinitely broken
but if floor is at a level where the eggs are safe
you only need to drop one egg to minimize the number of dropped and broken eggs ()

run a binary search tree (halving multiple times based on result) 
runtime: O(log(n))

if building[mid]:
  check_eggs()
  if eggs_broken == true:
  if building[mid]
    check_eggs(0)

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.
