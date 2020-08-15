#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - The loop could potentially run full length of n inputs.


b) O(n^2) - The for loop could run potentially n times, and the while loop could run potentially .5n times for each iteration of the for loop. So n * .5n potential runs, drop the constant and simplify to O(n^2)


c) No time complexity- There is no time complexity for something that can be infinite. And since time complexity is the "worst case scenario" the user could pass a negative number to this this function causing infinite recursion.

When used correctly: O(n) - Check if n(bunnies) == 0. If it does not, recursively call the function n-1 times. So it has a potential to run n times, given that the n is positive.

## Exercise II

Well since I live in a world where dropping an egg from waist height breaks the egg, I have to assume that my program world has much more durable eggs.  So I know nothing about those eggs, and where to reasonably start.

I'd start half way then.  So basically integer divide the total number of floors by two, to find about half way. Then drop an egg.  If it breaks, do the same thing for the bottom half.  It does not break, do the same thing for the top half.  Repeat until the floor is found.

Since I'm halfing my n every time, this becomes an O(logn) time complexity.



