#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

It's O(n), because the runtime is dependent on the size of 'n'


b)

It's O(n^2), because we loop through it twice

c)

It's O(n), because it's a recursive call on each item in bunnies

## Exercise II

I would first find the midpoint. 

If the egg doesn't break, the upper half needs to be checked, by adding + 1, until we reach a floor that returns that the egg breaks.

Else if the egg breaks, the lower half needs to be checked, by reducing -1, until we reach a floor that returns that the egg doesn't break.

Based on this, we can determing the highest floor that doesn't break and the lowest where it does.

Runtime is O(log n)