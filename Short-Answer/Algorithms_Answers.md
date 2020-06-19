#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) Runtime is O(n) because as the size of the input increases so does the runtime.

b) Runtime is O(n^4) which is a polynomial and you can tell this because it is a loop nested in another loop.

c) Runtime is O(n) recursive function will run once and then call itself for n-1 so the function winds up being called n times. It's based on the number of bunnies.

## Exercise II

    This sounds like a I could use a binary search recursively to minimize the amount of times the eggs break.

     1. Set a top floor = top_floor
        Set a bottom floor = bottom_floor
     2. Drop the egg from midfloor (top_floor - bottom_floor // 2)
    If egg breaks
        disregard top half
        make the midfloor the top_floor
        keep bottom_floor the same
        repeat 2 until egg doesn't break then return midpoint + 1
    else if egg doesn't break
        # disregard bottom half
        keep top_floor the same
        make midfloor the bottom_floor
        repeat 2 until egg breaks
        return the floor

The time Complexity is O(logn). A binary search keeps cutting the list in half.
