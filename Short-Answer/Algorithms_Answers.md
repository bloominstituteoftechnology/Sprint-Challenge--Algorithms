#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - You only have one simple math operation. An incerase in the input with not result in an exponential increase.  


b) O(log n) - the code is using one while loop. As the size of the input increases it will increase at a slow rate since only one loop is present. 


c) O(n) - the code is performing one recursive function. As the input increases it will always grow at the same rate. 

## Exercise II

My proposed algorithm to solve this would be a binary search. I would use a while statement that uses a top and a bottom to find the mid point of the floors. I would then use if, else if, and else statments to determine if the middle floor would result in a broken egg. If it did break I would eliminate the floors above the current floor and set a new mid point on the floors below. If the egg didn't break I would eliminate the floors below and set a new mid point on the floors above. I would continue this until the highest floor the egg would not break on was found and return the result.
