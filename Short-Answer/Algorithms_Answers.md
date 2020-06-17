#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
Since the while loop is n^3 and each loop adds n^2 it will almost always take n loops to complete. The Big O is thus O(n) or linear time.

b)
Since the first loop will take n loops to complete and the second loops grows exponentially to meet n, thus taking log(n) time the the final Big O should be O(nlog(n))

c)
The function will always return a value in approximately 2 commands so the big O is O(1) or constant time.

## Exercise II

I would use a method similar to a binary search, start at the middle floor, drop an egg. If the egg breaks all floors above can be ignored and try again at the floor in the middle of the floor chosen and the bottom floor. If the egg doesn't break all floors below can be ignored and a new one between the top floor and the middle can be chosen. Repeat this process until reaching a floor where the egg doesn't break but it does on the floor directly above it. Because of the continual halving of possible floors each attempt the algorithm should be O(log(n)).

