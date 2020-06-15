#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) a = 0 while (a < n * n * n): a = a + n * n. This algorithm runs in O(1) Constant Time


b) sum = 0 for i in range(n): j = 1 while j < n: j *= 2 sum += 1. This algorithm runs in O(n) Linear Time


c)if bunnies == 0: return 0

  return 2 + bunnyEars(bunnies-1)
  This algroithm runs in O(1) Constant Time

## Exercise II

Drop the egg from the middle floor. If the return value is "Egg Broke", move to the current floor minus one and try again until return is "Egg Not Broke"

If the return value from the middle floor is "Egg Not Broke", move to the current floor plus one until the return value is "Egg Broke"

Once the return value is "Egg Broke" move to the current floor minus one and return.

The runtime of the current implementation would be O(log n).

