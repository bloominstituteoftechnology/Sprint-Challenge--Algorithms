# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

This will compute while a < n, which means that the greater n is, the more times a will have to compute/be redefined. This would be considered linear or O(n).


```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
So this snippet has a while loop nested inside a for loop. So first we must loop through once for the range of n. This means the greater n is, the more times we must run through the first loop. The nested loop must be checked each time to compare j to n. I would say this is probably a Polynomial or O(n**2) because as the input increases, it affects the first loop linearly, but the inner loop executes if j < n, and j is initialized at 1. 


```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
In this function, the amount of bunnies/input is directly linked to the number of executions. The function will execute recursivly one time for each bunny. This function would be linear or O(n). 


## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

<!-- 

n = number of floors
>=f = egg breaks
<f = egg won't break

  To discover which floor is f, I would probably need to compare the the number of eggs broken for each floor.

  I would initially define f as the top floor.

  Then I would compare to other floors. Redefining f if I find a better floor.

  If the ratio of eggs broken to floor height is smallest, that means the floor is f. 

 -->

Because I would have to compare every floor, n is directly affecting the number of executions. Then I would have a nested if, to make sure f is still correct. So there would be 2 loops in this function. I would say this function would be in 0(n**2) or quadratic time.