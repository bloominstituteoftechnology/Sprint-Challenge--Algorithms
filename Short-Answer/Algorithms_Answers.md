# Sprint Challenge

**Please add your answers to the ***Analysis of  Algorithms*** exercises here.**

## Exercise I

Give an analysis of the running time of each snippet of pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

This block of code increases linearly along with increases to `n`. Thus `O(n)`.

```python
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

This block increases runtime by a factor of `n` for each increase in input of `n`. Hence `O(n)` notation would describe its time complexity.

```python
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

This block of code results in an output that is linearly related to its input. Hence `O(n)`

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

### Solution

My proposed solution to finding the floor `f` would look just like a binary search algorithm. I would first go to the middle floor of the `n`-floor building, and drop an egg. Depending on the egg breaking or not, I go to the next "middle" floor of the two halves of the building (the top half if the egg survives, the bottom half if cracked), and drop an egg again. It is through this approach-of halving my search space, checking a condition, and then halving again the half of the original search space I'm directed towards because of the condition-that I generally most quickly find `f`.

What's crucial about this binary approach is that my search space is **sorted**.
From `n`=0 -> `n`=`f`-1, my condition `egg will survive` is true. Every `n` above that inflection point is False; hence my search space is sorted.

This also assumes a uniformly random distribution of `f` for every `n`-level building. If there was a bias-that our eggs generally crack at lower stories-then another algorithm would be more appropriate, for instance starting at the ground floor and moving up.

The worst-case time complexity of the binary search is `O(log n)`. That's because at each step, we are halving the number of floors to check.
