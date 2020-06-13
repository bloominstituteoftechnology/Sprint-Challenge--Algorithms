#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  O(n). The loop takes n iterations.


b)  O(nlog(n)) - The outer loop (for loop) is O(n), because it is executed n times. And the the inner loop (while loop) is O(log(n)), because
 its runtime complexity is half of n, due j*=2.


c) O(n). The recursion takes n times.

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.


Description of the problem:

floors   0 . . . f . . n 

dropped  1 . . . 1 ....1  

broken   0 . . . 1 ....1


Planning an implementation:

It is better to use binary search for this problem instead linear search basically because it is more efficient and floors is a sorted list. The binary search algorithm will find the position of the target value within a sorted array, in this case the this value of floor such that the number of dropped + broken eggs is minimized. The table shows that this value is floor < f. 

"Floors" is a sorted list, the algorithm will recursively divides the problem space in half, ruling out half of the remaining elements with each jump. The rescursion will continue each middle floor, until the next middle floor that the egg is not broken. The worst-case time complexity of this algorithm is O(log n).

