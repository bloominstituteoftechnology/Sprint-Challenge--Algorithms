#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n^3): The n is the number of operations that the code has to perform and since n^3 is the largest operation out of the entire code block. 


b) O(n^2): With the use of the for loop the number of operations increases as the input size increases. 


c) O(n): This function is linear, recursion is used but that doesn't change the overall size of the operations.

## Exercise II

For this problem I would use a binary search, the reason being is that we have a general sense of where the eggs get broken and don't get broken. 

# start with the middle index which would  be floor f
# since we know that eggs don't get broken from "a-f" we  don't need to worry about those floors
# from floor f we can divide the floors in half if the right side has the higher range for damaged eggs then we can eliminate the right side and search the left. 
# since the floors are sorted this can be done. 

