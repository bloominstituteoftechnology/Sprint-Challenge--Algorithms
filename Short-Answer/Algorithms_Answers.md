#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime is O(n). Linear increase with every step, since the algorithm iterations reflect n directly. (see Algorithms_Questions for more details)


b) The runtime is O(nlogn). For inputs n=1 -->0, n=5 --> 15, n = 10 -->40, n=20 -->100 iterations. This follows a nlogn curve.


c)In it's current form runtime is O(1), since it's returning a constant value and not looping over anything. 

If the function is modified with an **else:** like:
def bunnyEars(bunnies):
    if bunnies == 0:
        return 0
    **else:**
      return 2 + bunnyEars(bunnies-1)

The runtime would be O(n). Since iterations would follow a linear line.

## Exercise II
Assuming the floors are a presorted list (0,1,2,3, etc.) I would take a binary search approach.
1. drop an egg at the n/2 th floor (where n is total number of floors), and note the result. 
   1. If the egg broke, we eliminate all higher floors as points of interest (irrelevant for f).
   2. If the egg did not break, we eliminate all lower floors as points of interest.
2. Each time we drop an egg we do so from the middle of the range in which we have interest.
   1. This means that on average we eliminate possible answers very quickly.
   2. The time complexity of this approach would be O(logn) where n is the amount of floors, the larger the building, the more floors we need to consider.