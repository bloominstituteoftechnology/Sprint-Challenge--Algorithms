# Exercise I
a) O(n) because the while loop interates once from 0 to n^3
b) O(n^4) because there are 3 for loops nested inside a for loop so it would be O(n) * O(n) * O(n) * O(n)
c) O(n) because it loops through the input -1 each time

# Exercise II
set the variables for drops. 
set the base cases for floors. floors = 0 return     0 floors = 1 return 1
divide the number of stories by 2 or //2 to find a midpoint and drop at the midpoint
if it breaks at the midpoint you know it's lower so check the lower half
if it doesn't break at the midpoint you know it's higher so check the upper half
from here you could iterate through floors - 1 or floors + 1 to find the where the egg breaks
you could also repeat the process of finding the midpoint and tetsing at that midpoint
