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
N and the runtime of the code will increase at the same rate. If the runtime complexity is dependent on n then it is linear. Giving us O(n).


```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
O(nlog(n))

We don't really care about the sum here, it won't really impact the function's complexity as n grows. So starting at the outer loop and one can see that the runtime is dependent on n itself, giving us a complexity of O(n). The inner loop, however, will have a complexity of O(log n) because j is rising exponentially. All things considered we end with O(nlog(n))  

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

O(n)

The number of times recursion is called depends directly on the size of n that one enters. It's similar to a for loop and so it's time and complexity reflects a linear rate of increase.

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

Binary Search Algorithm - O(log n)
We want to find the value of f while minimizing the breaking of eggs. To do this, a binary search algorithm would be a good approach. By starting at the midpoint of the number of floors and dropping the egg, we can look at the outcome and elimanate half of our range to search with one egg drop. If the egg breaks, we know that f is either equal to or greater than our midpoint and proceed. If the egg does not break, we can ignore all of the lower floors and proceed to search the higher floors and proceed. This would be a more time and resource efficient approach rather than dropping an egg from each floor one by one. 
