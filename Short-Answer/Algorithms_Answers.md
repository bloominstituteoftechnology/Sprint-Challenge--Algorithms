Add your answers to the Algorithms exercises here.
1. Run time is O(n). The operation will increase based off the value of n.

2. O(n logn), the length of n of the for loop will increase based upon the size of n.  In the while loop j increases at a rate times 2, therefore it will be log n.

3.Will be O(n).  Because it is recursive.


4. Egg 

We can determine f by using a binary search process.  The binary search process might eliminate the amount of dropped eggs, and has
only a slight chance of minimizing broken eggs.

We start with the middle floor and drop an egg.

Depending on if the egg breaks or not, we will do one of the following:
If the egg breaks, we drop an egg from the mid-floor, of a range, from lowest to the floor we just dropped the egg.
If the egg does not break, we drop an egg from the mid-floor, of a range, between the floor we just dropped the egg to the highest floor.

we will continue this process until we find a floor where the egg breaks one floor above a floor where the egg does not break.
worst case performance is O(log n)