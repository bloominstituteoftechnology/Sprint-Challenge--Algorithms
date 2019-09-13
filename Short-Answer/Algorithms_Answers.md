#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(n), a=n*n cancels out the n*n in the while loop, effectively make it while a<n: a=a+1


b)
O(n log n), the for loop is complexity O(n), and the nested inner loop is complexity O(log n)


c)
O(n), the recursive call is called once per n

## Exercise II

Start half way up the building, and drop an egg, if it breaks, go half way down from there and drop another.
when we have a floor where it breaks, and a floor where it doesn't directly below that, we have solved for floor f
This uses O(log n) complexity because we eliminate half of the floors with every egg drop
