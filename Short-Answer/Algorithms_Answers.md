#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) This loop was really hard but I think it works.
0(n)- the n*n inside the while loop cancels out an n*n in condition. while (a < n \* 1): a= a +1 does the same number of loops.

b) Now, this code normally would be a nested loop that has a time complexity of O(n^2) - but, since the nested/inner loop doubles every time we run it until it hits its maximum of n, the running time complexity is actually O(n log(n)). This is because the outer loop is time O(n) which is multiplied by its inner loop of O(log(n)).

c) O(n) - For more specificity this would actually be O(n - 1), the reason for this is because it is a recursive function. It is running linearly and subtracted by 1 each time the recursive call is made.

## Exercise II

To find the nth floor where the eggs don't break I can use a binary search that only goes down if the egg doesn't break, and up if it does. A Binary Search algorithm is an efficient method to use for this purposes, as it would have a running time complexity of O(log(n)). Following Poyla methods:

1. We will select a floor in the middle to start off on, and we'll throw an egg out the window to see if it breaks.
2. If the egg breaks, we know that the minimum floor where the egg will break is likely below us. We will resolve our dataset to only include the floors below us.
3. If the egg doesn't break, we know that the minimum floor where the egg will break is likely above us. We will update our dataset to only include those floors.
4. We will take our new "halved" dataset and choose a floor in the middle again; I will repeat the steps mentioned in points #2 and #3 above until my dataset contains two floors.
5. At this point, we'll either be on a floor where the egg has just broken or one where it hasn't (inside the remaining two floors). If n length is 2, I will return f dynamically depending on if the egg has just broken or not (using a simple if/else statement).
