#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)


b) O(n)


c) O(2^n)

## Exercise II


So this sounds like a binary search algorithim to me.

Which means we'd go to the middle of n and if the egg breaks, we'd go to the middle of the lower half etc etc, if the egg doesn't break we'd go up. The difference here is that I'd keep a last known good floor in case we end up going to far.


eggsthrown = 0
brokeneggs = 0
lastknowngoodfloor = none
floors = list of the range of n

while length of floors > 0:
    throw egg halfway
    if egg breaks:
        floors = bottom half
    if egg doesn't break:
        lastknowngoodfloor = current floor
        floors = top half

return lastknowngoodfloor