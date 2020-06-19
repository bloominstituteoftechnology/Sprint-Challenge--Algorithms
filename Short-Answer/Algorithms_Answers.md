#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Given n, it looks like the amount would double resulting a linear complexity. That being said, this would be O(n).

#Using O(2nk)
a = 0 
    while (a < n * n * n):
      a = a + n * n

b) O(log n), with given n, the loop will perform a single operation through the elements causing the runtime for b to be logarithmic.

#O(kn^3)
  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1

c) O(n), for a given n, the loop runs n times. It is similar to a for loop and will iterate until n == 0.

def bunnyEars(bunnies):
      if bunnies == 0:
        return 0 # O(1)

      return 2 + bunnyEars(bunnies-1) # O(n)


## Exercise II

I would go for a BINARY SEARCH given the runtime complexity of O(log n). 
Start at the middle floor, drop the egg and if it breaks, move down to the next floor.If it still doesn't break we can move up to the next floor. 
