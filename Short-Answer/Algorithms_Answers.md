#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) It's hard to say on this one because the n isn't given a value, but because the while loop will be calling 
    n*n*n, we could assume that the runtime there is O(n^3), because if n is high, it's going to add up extremely fast.
    In addition to that, the third line has a complexity of O(n^2) in addition to the O(n^3) in the while loop. Since
    O(n^3) is the highest, we'll go with that! 


b) In this one, since the first for loop takes O(n), and then the while loop inside also takes O(n), we multiply those together
    and we get O(n^2) as the complexity.


c) It is recursive, so it has the potential to make the time complexity pretty high, but the algorithm itself is quite simple,
    so the time complexity just ends up being O(n) since it's really just basic addition and subtraction. 

## Exercise II

def determine_the_floor(n, f):
    first step is to divide the floors in half and keep 
    --- each if equals an egg drop! --- 
    check to see if the halfway point (the lower bound of the top half) breaks the egg:
    if not:
        divide the top half in half (n - n//2) and do it again recursively
    if so:
        check if the floor you're on == f (the floor that eggs start breaking)
        if it is:
            return f
        if not:
            divide that bottom half in half (n//2) recursively and test again

    all of that runs until you find the value. You are getting rid of large chunks of floors
    and narrowing it down quicker than floor by floor working your way up. 

    because we have an if nested inside another, we have a runtime complexity of O(n*n), so O(n^2)