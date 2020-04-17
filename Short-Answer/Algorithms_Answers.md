#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
This code increases in a linear fashion which also increases n so example a would equate to 0(n)


b)
J theoretically affects the inner loop of this block and the doubling of n how ever we can break this down by identifying that this would be equal to log n, but like in the previous example the outer loop also increases in a linear fashion in regards to n so the two combined would give us 0(n*log n)

c)
This is simpler to A and acts in a linear fashion so the out put would again be 0(n)

## Exercise II

There are multiple answers to this question but i think two are prominent, 
The simplest and more long winded approach would be to to start at the first floor as would would have 2 eggs we could keep moving up the floors with using one egg to see which floor broke the egg this is a simple but potentially time consuming way to do it as we could potentially end up going up to the 100th + floor.

I think the best solution would be to use a binary search to find the floor that breaks the egg as this would save time, you could start at the middle of the n floor of the building and by using binary if the egg breaks we go down to the bottom half if it doesnt we go up to the top half and repeat. This would quickly allow us to quickly find the the floor 'f'. I also think with using binary the floors would have to be in order from 0 to -1 (n = 0 n = f -1 ).

Taking in to account that we are cutting the amount of floors/time in half i assume the time complexetity would be 0(log n ).

