#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

The operation is re-iterating over a number items in n, and increasing a counts. So, the time complexity for this is O(n). 

b)

This has a nested while loop inside of a for loop. But, the while loop is not incrementing by 1, rather it's being multiplied by 2. Which makes it in my opinion log n --> O(n) * log n --> O(n log n)

c)
The arithmetic is contant in the return, which is addin 2 for each time the function re-reruns. How many times the funcion will run recursively depends on bunnies input provided. For each addition incrementation in the input, the function will run one more time. Which makes it O(n)

## Exercise II

n --> number of story in building
f --> eggs broken if thrown from at least floor f
[f-1] --> eggs doesn't break

Challenge --> find floor #f, from which if egg is dropped then it will break
        --> if dropped from zero, the egg will not break
        --> if dropped from n floor the egg will break

Solution:
    I will use binary search to find the mid point by dividing (0+n)/2. and test if it breaks
    if breaks, then do binary search on the left side to find lower floor
    and then binary search on the right or left side

    I will use while loop, and if conditional statments to find the f

Time Complexity: 
    O(log n) --> since the iteration will not be on every element of n
    
