#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) a = 0
    while (a < n^3): ## O(n**3)
      a = a + n^2 ## O(n**2)

     runtime complexity: O(n)
     The while statement is O(n^3), but a approaches the conditional more rapidly than this because a also increases exponentially (O(n^2)). The second runtime complexity is subtracted from the first to get O(n).


b)  sum = 0
    for i in range(n): ## O(n)
      j = 1
      while j < n: ## O(n * 1/2)
        j *= 2
        sum += 1

    runtime complexity: O(n^2)

    The first for loop must run through all n range (O(n)). The while loop also runs through the whole n range, but it's slightly better than the first loop: it is actually only O(n/2). However, big O notation disregards this relatively small improvement, so the total runtime complexity is O(n^2).


c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

    
    runtime complexity: O(n)

    The function is called recursively as many times as there are bunnies. Once you run out of 'n' bunnies, the function stops.
    Therefore the runtime complexity is O(n).

    

## Exercise II


This seems like a good use of a binary search algorithm.

number_of_floors = n
target = f (which floor)

The broken eggs are not a variable- rather they represent the runtime complexity of the algorithm. %%time.

If the number of floors is one, the target == 1.

If n is greater than one, find the middle floor. Drop the egg off the floor. One of two things will happen:

    If the egg breaks, that floor you just dropped it off becomes the new top of your height range. Find the middle floor between the ground floor and the floor you just dropped it off. 

    If the egg is intact, the floor you just dropped it off becomes the new bottom of your height range. Find the middle floor between the floor you just dropped it off and the top of the building.

Repeat these steps until the range of floors left to test equals one. Then you have found your target floor.

This is a nice solution because the runtime complexity (aka the number of eggs dropped) is equal to O(log(n)) (That's log base 2). Even if you have a building with 10,000 floors, you will divide the number of floors in half each time, so it would only take a maximum of 14 eggs.

