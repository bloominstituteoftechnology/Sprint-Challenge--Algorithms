#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) I believe that is code has a run time complexity of O(n) because it has to loop over and over
until a is less than n^3. 


b) This code is O(n log n), the first loop happens n times and the second loop happens until j is less than n but j 
isn't linear while it's looping, the second loop is completing faster than the first loop as n increases


c) This function is O(n), n is being decrimented by 1 each time the function recurses. So it will recurse n times 

## Exercise II

Throw an egg off floor n/2, if it breaks drop an egg off the middle of the floor beneath floor n/2. If it doesn't break drop and egg off the middle floor of the floors above, repeat this process until you are out of floors to jump to. If it broke on that floor that is f, if it didn't break f is one floor up. 

The time complexity of this algorithm would be O(log n) because this is pretty much just binary search and bineary search is O(log n)

