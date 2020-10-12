# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```
O(n)

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
O(n * log(n)) = O(nlog(n))

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
    
```
O(1^n)
## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.


def egg_death(n, start=None, end=None):
    if start and end are None # is this is base
        # assign 0 for start
        # assign n for end
    # the floor = start + high - low // 2 (midpoint)
    # drop egg at the floor
    # if egg drop on the floor returns it's broken
        # if egg drop on the floor - 1 returns not broken
            # return the floor <-- Base Case (what is?)
        # else
            # call egg_dewath, start is start and end is the floor
    # else
        # if egg drop on the floor + 1 returns broken
            # return  the egg + 1
        # else
            # call egg_death start is the floor and end is end
    # scrambled heat death = the universe ends