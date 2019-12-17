#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Would be runtime of O(n) because it is dependent on the n alone, with one for loop.


b) Would be O(n^2) because although the while is still a loop, and it is nested inside the for loop.


c) O(n) because although there is no for loop, the recursion is still depending on the n.

## Exercise II
This can be done as O(n)

def safeFloor(n)
dropped = 1
broken = false

While (broken == false AND dropped <=n):
    drop egg from dropped
    if egg breaks:
        broken = true
    else:
        dropped =+ 1

if dropped == 1
    return 0
elif dropped > n:
    return "Egg didn't break"
else:
    return dropped