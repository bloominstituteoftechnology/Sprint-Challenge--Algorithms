#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Assuming A is being incremented somehow so that the while loop ends eventually this should be O(n) since canceling out extra terms with division: n ** 3 divided by n ** 2 is n.


b) The first loop is O(n) and the second is O(log base 2 n) so multiplied together its O(n log n)


c) This is O(n) since it is just called n times until reaching base case.

## Exercise II

So with only one egg, we could only do the naive solution by moving up one level at a time and trying again until it fails which would be a O(N)

If we have infinite amount of eggs, the easiest approach would be to do is a binary search. I would start at the halfway point of the building and then pick lower or higher depending on if it doesn't or does break.

For Example:

    1) Begin at halfway point and drop the egg
        a) if it breaks, new halfway point is between old halfway and bottom
        or
        b) if it doesn't, new halfway point is between old halfway and top

    2) recursively do this until:
        a) distance between old halfway and new halfway is 1
        AND
        b) old halfway is a break and new halfway is a save
        
     then
    3) RETURN the latest new halfway is the highest floor that eggs don't crack
