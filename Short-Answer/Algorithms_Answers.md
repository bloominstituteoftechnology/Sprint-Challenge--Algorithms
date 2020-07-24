#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
a = 0. While a is less than n**3, a = a*n^2

This code will always result in an infinite loop given that a is 0. if a=1, code is O(n)

b)
sum = 0. for i in range(n), initialize j to 1, while j is less than n, double j and add 1 to sum

The for loop in this case gives us O(n), and the while loop, given that it's a doubling sequence, gives us O(log n). Final complexity is O(n log n)

c)
Recursive. If bunnies == 0, return 0. Else return 2 + BunnyEars(n-1).

If I'm not mistaken, this should be O(n) because the recursion doesn't have any branches.
It also seems like a silly use of recursion considering you could just do n*2 

## Exercise II

Start at the ground floor

Find the middle point between the start point and top floor. 

while f has not been found:
    
----Drop the egg

----If the egg breaks:

--------Move to a middle point between current location and current lower bound (default ground). Set current floor as the upper bound.

----If the egg does not break:

--------Move to the middle point between current location and higher bound (default top floor) Set current floor as the lower bound.

return floor f 

This is a binary search, so the runtime complexity is O(log n)
