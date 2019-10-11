# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```


```func(n):
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

my strategy would be thus: 

start at the middle floor of the building and drop an egg.

***step 1*** if the egg breaks: begin again at the *midpoint* between the current floor and the *ground floor* and drop another egg.
  ***step 2*** if the egg breaks: ...... 
    ***step 3***  if the egg breaks: ......
    ***step 3***   if the egg does not break: ......
  ***step 2*** if the egg does not break: ......
***step 1*** if the egg does not break: begin again at the *midpoint* between the current floor and the *top floor*

repeat this process until EITHER:

a). An egg breaks, and you move down a single floor, where the egg does not break. The current floor is the "floor f" we are seeking.

b). An egg does not break, and you move up a single floor, where the egg does break. The floor below (where you just were) is the "floor f" we are seeking.