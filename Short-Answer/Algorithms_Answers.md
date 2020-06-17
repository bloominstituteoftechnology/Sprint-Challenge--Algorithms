#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0 #constant time, O(1)
    while (a < n * n * n): #linear time O(n)
      a = a + n * n #constant time O(1)
```
### O(1+ n + 1) = O(n)


```python
b)  sum = 0 #constant time, O(1)
    for i in range(n): #linear time, O(n)
      j = 1 #constant time, O(1)
      while j < n: #normally linear time, but j is defined outside of the function; O(logn)
        j *= 2 #constant time, O(1)
        sum += 1 #constant time, O(1)
```
### O(1+ n*(logn*(1+1))) = O(1+n*(2logn)) = O(1+ 2nlogn) = 0(nlogn)

```python
c)  def bunnyEars(bunnies): #constant time, O(1)
      if bunnies == 0: #constant time, O(1)
        return 0 #constant time, O(1)

      return 2 + bunnyEars(bunnies-1) #recursive call, treat like a loop; linear time O(n)
```
### O(1+1+1+ n) = O(3 + n) = O(n)

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.


building, stories/floors = n
if egg thrown off floor f or higher, then broken
if egg thrown off floor less than f, then not broken
when on floor less than f, throw eggs otherwise don't throw...?

O(n) assuming I'm looping and iterating through the floors, only throwing an egg when on floors less than f
