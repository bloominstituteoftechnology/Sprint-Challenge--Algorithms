#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
 first line is a constant O(1) can be disregarded in respect to the while loop
 While loop will run O(n^3) times yet a will grow at the speed of n^2. The while loop test logic will be approximately how fast can n squared catch n cubed. n^3/n^2 = n 


b) O(NlogN)
sum is a constant O(1) and can be disregarded in this case
i is O (n), j is doubled each time in the while loop, this gives  O(logN) run time to reach target.
n * logN




c) O(n)
 recursuvce case only calls itself one time, performing a constant check and addition each step.

## Exercise II

assumption:
 -egg has equal durability 
 -Egg has two state : broken and not broken

To minimize the number of eggs dropped and lost, we should start in the middle of the building (N/2). Depending on the state of the egg, we decide we need to go upper half or lower half. In either case, we then divide the number of remaining floors in half again and repeat the experiement till the remaining floor is less than 1. 

This would be O(log(n))

