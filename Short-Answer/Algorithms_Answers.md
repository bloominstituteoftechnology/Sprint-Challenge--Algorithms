#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

Parentheses first
Exponents (ie Powers and Square Roots, etc.)
Multiplication and Division (left-to-right)
Addition and Subtraction (left-to-right)

a)  a = 0
    while (a < n * n * n):
      a = a + n * n

This code will run in O(n) time; Linear time

The loop is running n^3 times. The assignment to a is increasing by n^2. The exponents of n cancel each other out leaving the loop running in direct proportion to the size of n.

b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1

This code will run in O(n^2) time; Polynomial time.

For loop occurs n times. While loop occurs 1/2*n times. Multiplying the outer loop by its body (O(n)), this gives us O(n^2).

c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

This code will run in O(n) time; Linear time

The function will be called n times. The +2 doesn't occur until the recursive calls unwind. Therefore we can ignore the +2 and note that each recursive call subtracts 1 from n and calls the function again. 

## Exercise II

This is a binary search algorithm. We'll keep dividing n (number of floors) in half (higher if it doesn't break; lower if it does) until we find the breaking point.

This code will run in O(log 2 n) time; 

divide total number of floors in half
    does egg break?
        Yes, we need to go lower -> (floor we're on      - prior lowest floor) / 2 + prior lowest  floor.
        No, we need to go higher -> (prior highest floor - floor we're on)     / 2 + prior highest floor.
        If floor equal 0 then we're done; otherwise, call again. 