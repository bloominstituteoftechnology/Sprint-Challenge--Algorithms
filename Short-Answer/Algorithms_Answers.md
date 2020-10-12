#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) because of the while loop


b) O(n^2) because of the two loops 


c) O(n) because this one calls itself recursively

## Exercise II

I would use a binary search to minimize the number of broken eggs. 

start = 0 
end = len(f) 
mid = (start + end) // 2

By starting at the middle of all the floors, we can see whether or not the egg breaks at the mid level of the building. If it breaks, eliminate all the floors above the middle floor and repeat until it does break. If it doesn't break, eliminate all the floors below that floor and repeat. Runtime for the binary search is O(log n) because every time we run it we're cutting in half the number of options