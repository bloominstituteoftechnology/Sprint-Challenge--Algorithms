Add your answers to the Algorithms exercises here.

a) O (N) - You loop through while a is less than n ** 3, but every time you add n ** 2 to a so it comes out to O (n) because you can cancel out the n's.

b) O (n ** 4) since there are four nested for loops each one is O(n) when you drop the constant because you dont go through the entire range of n in the nested for loops but that doesn't matter.

c) The recursive function is being called recursivley n times before it reaches its base case of 0 so it is O (n)


Exercise II
- I would use binary search to figure out what floor which would be o (log n). I would start on floor n/2 and then adjust the low and high depending on the result and keep trying the middle till I found the floor. 