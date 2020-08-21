#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

O(n)
N and the runtime of the code will increase at the same rate. If the runtime complexity is dependent on n then it is linear. Giving us O(n).

b)

O(nlog(n))
We don't really care about the sum here, it won't really impact the function's complexity as n grows. So starting at the outer loop and one can see that the runtime is dependent on n itself, giving us a complexity of O(n). The inner loop, however, will have a complexity of O(log n) because j is rising exponentially. All things considered we end with O(nlog(n))  

c)

O(n)
The number of times recursion is called depends directly on the size of n that one enters. It's similar to a for loop and so it's time and complexity reflects a linear rate of increase.

## Exercise II

Binary Search Algorithm - O(log n)
We want to find the value of f while minimizing the breaking of eggs. To do this, a binary search algorithm would be a good approach. By starting at the midpoint of the number of floors and dropping the egg, we can look at the outcome and elimanate half of our range to search with one egg drop. If the egg breaks, we know that f is either equal to or greater than our midpoint and proceed. If the egg does not break, we can ignore all of the lower floors and proceed to search the higher floors and proceed. This would be a more time and resource efficient approach rather than dropping an egg from each floor one by one. 
