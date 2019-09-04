#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Growing linearly since it doesn't get modified. O(n)

b) There are two loops and O(n) gets multiplied by itself resulting in O(n^2).

c) Recurvsive algorithm tells you what to return explictly. O(n)

## Exercise II

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
    return "Egg didn't brake"
else:
    return dropped

O(n); could also be written as binary search with a runtime of O(log n)


