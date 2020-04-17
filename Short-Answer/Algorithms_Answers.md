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

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.


 return 0

 There's no constraint on the question asking for f to be maximized, and 0 is the lowest positive integer value, so you can't get lower than that to drop your eggs. Therefore, we've minimized the number of dropped + broken eggs to 0. The time complexity of this is O(1) as the algorithm doesn't change via the size of the input.


 ```
 def eggDropBreaks(floor):
     # drop an egg
     # if it breaks, return True
     # else return False

 def findHighestNonBreakFloor():
     # set f to 0
     # loop over the following
         # drop an egg from current value of f
         # if it doesn't break
             # increment f by 1 and repeat the loop
         # else
             # return f - 1
 ```

 the runtime complexity would be O(n) where n = f as the algorithm will scale linearly as f increases.
