#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This has a time complexity of O(n). The variable (a = n * n) will cancel out the others making the while statement (a < n). 


b) This has a time complexity of O(n^2). The nested loops will create an exponential time increase based on the inputs.


c) This has a time complexity of O(n). As n increases so will the time it takes to calculate the number of ears.

## Exercise II

The best approach for this would probable be a binary search(broken egg or not broken egg) which would give it a time complexity of O(log n). Start from the middle and if the egg breaks we know we need to go to lower floors and vise versa. For the code we could set up a "while" statement for the eggs state. Then have it divide the number of floors available and divide by two. If the egg doesnt break take the upper half of whats left in floors and repeat and do the opposite if it does.