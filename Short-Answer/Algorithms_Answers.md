#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)O(n) - value of a will increase as the size of n  will increase, this will increase the while loop condition to run the loop


b)O(nlogn) - first loop time complexity is O(n), but the the second loop run for  almost half of the value of n. so total runtime complexity would be O(nlogn)


c)0(n) - recursion of the function depends on the size of n

## Exercise II

1) start from the middle floor f = n//2, 
2) drop a egg
3) check if the egg is broken or not
4) if egg is  broken repeat  the same process for the left subarray of   n//2(0 to f-1)
5) if egg is not broken repeat the process for  the right subarray of   n//2(f+1, n)
6) Repeat step 1 to 5 until n = 0 or n= n

Runtime complexity for this solution will be O(logn)


