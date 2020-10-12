#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n^3) because its length is dependent on n multiplied by itself 3 times.


b) 0(n log n) because it goes one loop dependent on length of n and a second that is a subset of n.


c) O(n) because it is running through "bunnies" aka our "n" once until it is 0.

## Exercise II

Divide the number of floors in half and toss the egg.
If it doesn't break repeat with taking the middle of upper half of floors (middle to last and keep changing the middle)
If it does break repeat with taking the middle of the first half of floors (first to last and keep changing the middle)

This will be 0(log n) because we are dividing n into smaller sets and not checking all n
