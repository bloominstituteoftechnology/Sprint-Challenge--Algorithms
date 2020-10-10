#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n). As n gets larger, the number of cycles that the function will run is n. because the while condition grows a rate of n^3 and the function adds n^2 each iteration, it will hit the condition after 'n' cycles.

b)O(n log(n)). This function creates a for loop, but also has a limiting variable in 'j'. As n gets larger, the function will loop more times, but n will need to grow by a factor of 2 to overcome the condition set by the 'j' variable in the while loop. 


c)O(n). This recursive function calls itself on on the input value minus 1, so it will run 'n' number of times, the addition in the return statement is constant time, so it is disregarded.

## Exercise II
I would use code similar to a binary search. 
First I would find the middle floor of the building, and throw an egg from that window and check to see if it is broken. If it is broken, then I would run the same test, but for the bottom half of the building, starting the the middle of the bottom half. If the egg was not broken, then I would move to the top half of the building and run the same test. This would repeat until the floor is found where the egg is broken if dropped, and if dropped from that floor-1 is not broken, then that floor-1 is returned.

The time complexity of this search is logarithmic time, since as the imput size(number of floors) gets larger, the program will run longer, but not in a directly proportional way to the imput size. Since we are only looking at half of the tree each time we run the function, the runtime is logarithmic.

