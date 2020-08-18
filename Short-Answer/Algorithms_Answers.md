#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)O(n) - value of a will increase as the size of n  will increase, this will increase the while loop condition to run the loop


b)O(n^2) - there are two loops that depend on the size of n


c)0(n) - recursion of the function depend on the size of n

## Exercise II

1) start from the middle floor f = n//2, 
2) drop a egg
3) check if the egg is broken or not
4) if egg is  broken repeat  the same process for the left subarray of   n//2(0 to f-1)
5) if egg is not broken repeat the process for  the right subarray of   n//2(f+1, n)
6) Repeat step 1 to 5 until n = 0 or n= n

Runtime complexity for this solution will be O(logn)


