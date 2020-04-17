#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime grows by n each time the input size grows by n, the runtime grows linearly so O(n). There is only one loop so this makes sense. 


b) The runtime grows exponentially each time n increases linearly so the time complexity is O(n**2). There is two loops so that makes sense. 


c) The function calls itself recursively which causes the runtime to increase by factorial n each time n increases linearly. The time complexity is O(n!). 

## Exercise II

We don't know at what floors the eggs break, but we do know that all the floors above a certain floor they do break. 
So this looks similar to the binary search problem. 

Instead of looping through each floor which would waste eggs, we should test the middle floor with one egg. 

If it breaks there then we test again at halfway point between there and the lowest floor. If it doesn't break there then test again at the halfway point between that floor and the middle floor. 

If the egg breaks we move down
If it doesn't break we move up

Each time we move to the middle floor between the floor we just tested
and the middle. 

Iterate this process until the outcome changes when we move by just one floor. 

The runtime of this algorithm is O(log_base_two(n)) because it is the inverse of exponential time. As n increases linearly the runtime decreases exponentially, because the places we have to search is halving each time. 
