#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) -> the number of times the loop needs to run is directly proportional to the input of n.


b) The inner loop has a runtime of O(log n) since the iterator doubles with each run, so the number of runs is half the range. 

The outer loop has a runtime of O(n) as the size of n directly increases the number of times the loop will run.

When we combine these runtimes, we get an overall run time of O(n log n)


c) O(n) -> This will be a linear runtime as the input size of `bunnies` will directly increase the number of times the function needs to run

## Exercise II
I think using a binary search would minimize the number of eggs that get broken during the testing. Since each test will remove half of the potential floors that would lead to an egg break. 

start = 0
end = len(f)
mid = (start + end) // 2

By starting at the middle of all the floors, we can see whether or not the egg breaks at the middle level of the building. If it breaks, eliminate all the floors above the middle floor and repeat until it does break. If it doesn't break, eliminate all the floors below that floor and repeat.

By using this approach, we can have a runtime from binary search of O(log n) as each subsequent run halves the total number of options.

