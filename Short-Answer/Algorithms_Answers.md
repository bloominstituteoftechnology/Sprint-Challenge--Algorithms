#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(N), because it's like a for loop that goes till n^3, but each step is n^2, so the loop will always take n increments to complete. For example, for n=2 the loop ends around 8, but increments by 4 every time, so 8/4 is 2, or n. It took n times to complete.


b) O(log(N)), because we have two loops multiplied together. The first loop is n, and the second loop is log(n), so n * log(n). The reason the nested while loop is log(n) is because its runtime complexity is halving every time, since j*=2.


c) O(N), because this acts like a fancy for-loop. It starts at n and increments down by one until n is zero. Every time it calls itself again, it decreased the number of loops left by one. The loop will always occur n times.

## Exercise II

I'd use a version of binary search to solve this, since we get to use an ordered list ("floor zero to n floors"). The runtime complexity of this solution will be O(log(N)), since the amount of area we have to search halves at every iteration.

So the function would take n floors and I'm guessing there'd also be a function provided to us who's interals we aren't allowed to see. This helper function simply checks whether our function's output is equal to f. Since we're not supposed to know what f is.

So my recursive function would find the middle of our original list (range(0,n+1)), or prev_list.
Then it would run the helper function on middle, to see if an egg dropped from that height minus one would break.
If the egg breaks, then I get the middle of the new list of everything below the previous middle (prev_list[:middle]) and try again.
If the egg does not break, then I get the middle of the new list of everything above the middle (prev_list[middle:])
I repeat this process until the length of the list we're working with is one, because that element is f.

I'd need to use some floor division for finding the middle, pass the list into each recursive call of my function.
Could improve the space complexity by just using n instead of a list made from n. And have the base case be n==1.




