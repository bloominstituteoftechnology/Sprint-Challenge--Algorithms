Add your answers to the Algorithms exercises here.


## Exercise I

a) The time complexity is O(n) since the while loop will always run n amount of times.
b) The time complexity is O(n^4) as each iteration will roughly take n amount of times.
c) The time complexity is O(n) since the function will recursively be called bunny-number of times.

## Exercise II

A naive solution would be to move up the building and drop an egg from each
floor and determine _f_ once an egg is broken. E.g. in a 10-story building and 
_f_ being 9, we'd have to drop 9 eggs.

A better solution would be to divide the _n_ of stories into half and drop 
an egg at the midpoint. If it breaks _f_ is lower than the midpoint, so 
we can check the lower half of _n_, else if it doesn't break we can check the 
upper half. For either the upper or lower half we repeat the above process
(get midpoint and drop the egg). E.g. in a 10-story building and 
_f_ being 9, we'd have to drop 4 eggs (drop at 5th floor -> not broken, 
drop 7th floor -> not broken, drop at 9th floor -> broken, 
drop at 8th floor -> not broken --> 9 is _f_).
