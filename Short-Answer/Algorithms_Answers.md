#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) since there is only one loop, even tho we are checking a < n^3 the time complexity would be O(n)


b) There are two loops, one checking for length n and one checking j < n, so this one would be O(n * j)


c) with this function, it is being called n times until it reaches it's base case so the complexity is O(n)

## Exercise II

from 1 throw an egg every n/3 floors:
    throw count += 1
    highest = 0
    if the egg breaks:
        from the current floor to the highest checked floor:
            throwcount += 1
            if the egg doesnt break
                return current floor
    else:
        highest = current floor

i believe this function would be somewhere close to O(nlogn)
