#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)O(n) The while loop is going until a is greater than or equal too n cubed, but n squared is added to it each time. 
Therefore The loop will only run n times.


b)O(n log(n)) There are two loops in this to be considered. The first is a for loop in the 
range of n which will run in O(n) time. The second is a while loop that is constantly doubling j for every
time it goes through the loop, and it will run in O(log (n)) time.
This leaves us with O(n) * O(log n) which is O(n log(n)) time.


c)O(n) Even though this function uses recursion, it only calls itself once, which leaves it linear time.

## Exercise II


When it comes to considering the problem of n stories and finding the story where the egg drops and doesn't break anymore
The best answer is to constantly cut the number of floors to search in half. This will give us O(log(n)) time.