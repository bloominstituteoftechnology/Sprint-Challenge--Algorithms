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

number_of_eggs = some number
n = some number
f = some number

call a function find_the_floor(n, f):
    n = n // 2 <---- divide the number of floors in half to determine if f is in upper or lower bound
    drop one egg
    if div is less than f (or in other words, if the egg doesn't break):
        div = 



