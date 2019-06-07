Add your answers to the Algorithms exercises here.

```
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```
Answer: This is O(n^3) complexity because even if oupputting 'a' requires a+n*n, the while condition evaluates until n^3 is fulfilled. 
```
b)  sum = 0
    for i in range(n):
      i += 1
      for j in range(i + 1, n):
        j += 1
        for k in range(j + 1, n):
          k += 1
          for l in range(k + 1, 10 + k):
            l += 1
            sum += 1
```
Answer: This is also O(n^3) because each loop requires n (except for the last one which is cosntatnt). Thus the complexity is also grows with each loop.
```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
Answer: This is O(C). Even if it;s recursive method, it's complexity is constant because all it returns is the number added by 2. 

## Exercise II

Suppose that you have an _n_-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get broken if dropped off a floor less than floor _f_. Devise a strategy to determine the value of _f_ such that the number of dropped eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode and give the runtime complexity of your solution.

Answer:

The Problem:
-----------
Finding an optimal value of f such that the number of dropped eggs is minimzed

Understanding:
-------------
plenty of eggs = n 
n can sufficiently large
n can only be an integer
n is always positive
f is a postive height 
let's keep f an integer


Analyze:
-------
we can create a threshold for f e.g. f = 0: 
if f == 0:
return n 
meaning that if we are on the ground, no eggs will be dropped or broken. 
but if f <= 1:
return 0
the egg wouldn't get broken 
for f-1 condition
we can have two inputs to the function:
    1. number of eggs (n)
    2. the floor (f)


I think this will be O(1) complexity. 