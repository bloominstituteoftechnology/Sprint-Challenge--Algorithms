#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)

b) O(n*log(n)) 

c) O(n)

## Exercise II

It seems logical that the binary search algorithm be used because this sort method does wonderfully for finding the value v in a set of numbers n.  The search will cut lenghths of the building in half repeatedly until it zeroes in on the final value.  The time complexity would be O(log(n)

Find total height of building - set midpoint.
Check if midpoint breaks an egg.
    If midpoint does break an egg
        set new height of building to be the bottom half of what you tried previously
        Keep checking if egg breaks and repeat cutting slices in half either above or below your midpoint
    if midpoint does NOT break egg
        set new midpoint to be the midpoint of the upper half of the previous building's height.
        throw egg from THIS midpoint
        repeat process going to upper or lower half of the 'new' building's height until the max height is found