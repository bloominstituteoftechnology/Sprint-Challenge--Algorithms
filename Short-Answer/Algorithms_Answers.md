#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) - The size of n equals how many iterations the while loop will run before exiting.

b) O(n logn) - The outer for loop is O(n) since it increases linearly as n increases. The inner while loop only executes sometimes when n is large enough (i.e. at minimum 2). So this would be O(n) + O(logn) = O(n logn)

c) O(n) - This runs n times before reaching the base case.

## Exercise II

Brute force attempt:
Start from ground floor and keep going up until first egg breaks. Time complexity O(n)

Potentially better solution:
Start at floor 10 and increment floor by 10 until egg breaks. If egg breaks on, for example, floor 30, then check floor range from 21-29 to see which floor it breaks on. Time complexity O(logn)
