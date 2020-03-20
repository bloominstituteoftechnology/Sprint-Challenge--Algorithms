#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
Because this is a while loop it is necessary to analyse what is being done within the loop itself to determine the complexity.
Since the number of times this operation will run based on the size of n due to the calculation in the while loop  The larger size of n the longer it will take: O(n)


b)
There are three operations that are based on the size of n:
1. The for loop runs for each n: O(1)
2. The while loop grows and reaches n twice as fast in each run:  O(log n)

sum = 0 is a constant and can be discarded
j = 1 is a constant and can be discarded
j *=2 is a constant and can be discarded
sum += 1 is a constant and can be discarded

c)
This recursive function would have a time complexity of O(n)
If there are no bunnies nothing happened.
The calculation in the return does not impact the complexity because it does not change the n.


## Exercise II
floors = [0] * n
thrown = min value for floor where eggs won't brake if thrown
dropped = d max value for floor where eggs won't break if dropped

for f in range(n)
    broken = 0 # number of eggs broken
    if f <= thrown or f > dropped
        broken = broken + 1
    floors[n] = broken
return min(floor)

I believe this algorithm would have a complexity of O(n^2)

