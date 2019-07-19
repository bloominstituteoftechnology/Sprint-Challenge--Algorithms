# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```
**O(n^3)**, the while loop evaluates until a is evaluated n times which in this case is 3 because there are 3 n's in the while loop condition.
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
**O(n^3)** Each loop requires n before the last one which is a constant so we drop it when calculating O
```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
**O(Constant)** I think? It just recursively returns the number addded by 2

## Exercise II

Suppose that you have an _n_-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get broken if dropped off a floor less than floor _f_. Devise a strategy to determine the value of _f_ such that the number of dropped eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode and give the runtime complexity of your solution.

----------
unknown value of eggs = n
f cannot be negative because no negative height on a building to the floor
declare discrimantory value to measure if eggs were broken? or how broken they were? if this were to make it more complex idk but you can just assign booleans i guess

threshold f in a while loop f++ such that once f evaluate to False min(f) is the floor that eggs start breaking.
