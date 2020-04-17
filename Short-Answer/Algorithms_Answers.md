#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) a = 0
    while (a < n * n * n):
      a = a + n * n

    - O(n^3)
    - The while loop determines how many times the code will run and because it is n * n * n which is the sames n^3.
    - As n increases in value the result will grow exponentially.


b) sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1

    - O(n log n )
    - As n increases the outer for loop increases linearly, but the inner while loop runs O(n) because as you double j, n is halving.


c) def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

    - O(n)
    - this algorithm is linear because as a certain amount of bunnies are added the code runs a certain amount of times.

## Exercise II


