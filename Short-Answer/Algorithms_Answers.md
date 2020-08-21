#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(n^c) Polynomial time. The inner functions seems to be efficient code, but the outer while loop will greatly increase the number of operations.


b)
O(n log n) Linearithmic. The outer and inner function add to the runtime, but the innter function does so significantly less.

c)
O(n) Linear time. while going through each recursion, each call is only being operated on once. There are only n number of operations.


## Exercise II

Start on the middle floor to see if the egg breaks. If it doesn't, you can jump to the next mid point of the remaining floors above and repeat until the egg breaks. From that point you could then check the floors below to find F's value. This would allow you to cut the number of eggs you throw out by possibly half. Worst case scenario you could end up throwing out O(log n) eggs.




