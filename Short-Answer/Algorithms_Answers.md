#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
> The loop range is n³, but n² within each loop. The difference is n.


b) O(n log n)
> Outer loop is n, inner loop is log n because the pointer is doubled each loop.

c) O(n)
> Uses recursion but each call only has one recursive call. Like a single for loop.

## Exercise II

> To mitigate only for breaking eggs, use a linear search. The array would be sorted from lowest floor to highest. Loop through, moving higher and higher. Only one egg would break when it does, that would be the f floor.

> To minimize broken eggs and time, you could use a binary search. Log n time. Divide the array / building in half and check the midpoint for a broken egg. Also check the floor below. If one egg breaks and the other doesn't, the one that broke is f. Otherwise they will either both break or not break and that will indicate that you need to move higher and lower, and restart with the midpoint of everything above or below that point.