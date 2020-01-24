#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) If we are to assume that n = len(whatever we're working with), then the running time should be O(n). Everytime the while loop is evaluated, we check to see if a < n^3 and if it is, we increase a by n^2. Thus, time complexity = O(n)


b)The running time will be O(n^2) since the for loop is O(n) and the while loop is O(n-1) which is close enough to O(n). **Actually O(nlogn) because the second loop cuts n in half.**


c)The time complexity would be O(n) since for the value of bunnies, we would recursively call bunnyEars the same number of times as the value of bunnies.

## Exercise II

# Merge sort method
I would start at n/2 floor.
if the egg breaks
    I would go down to n/4 floor
    recursively call the function with a new n and same bottom floor

else
    I would go up to 3n/4 floor
    recursively call the function with a new bottom and the same n.

The time complexity on this method would be O(n log n)