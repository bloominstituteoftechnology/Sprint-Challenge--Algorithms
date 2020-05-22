#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
This function runs in O(n) time (or "linear time"), 
where n is the number of items a is less than n * n * n. If a is less than n * n * n 10 times, 
we have to do a = a + n * n 10 times. If it's less 1000 items, we have to continue 1000 times.

b)

O(n^2)

Here we're nesting two loops. 
If our array has n items, our outer loop runs n times and our inner loop runs n times 
for each iteration of the outer loop. Thus this function runs in O(n2) time (or "quadratic time"). 

c)
0(n)

We iterate through the number of bunnies


## Exercise II

start at middle of the building, drop egg, if egg does not break, you can eliminate all of the buildings below,
if egg breaks, you can eliminate all of the buidlings above. Continue to do this until f is found

O(logn)


