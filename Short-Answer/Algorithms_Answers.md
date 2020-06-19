#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)

because: O(n^3) / O(n^2) = O(n)


b) O(n log n)

because: O(n) * log M = O(n log n)


c)O(n)

because: It only performs 1 function, if bunnies == 0, return 2 + bunnyEars(bunnies-1)
doesnt matter the hight of the interger input, it will still run the same operation.

## Exercise II

Binary Search - O(n)

take the total number of floors and divide by 2 (n/2), and drop an egg, if it breaks, go to N-floor middle (n - middle) / 2, and drop another egg from there, and repeat until the egg doesnt break, and that n-floor becomes your value for F.  when you divide the total available floors by 2 essentially determining which half of the floors the answer is in.  which brings your efficiancy up, since your disregarding half of the possible floors and makes it much quicker than starting at the top and dropping an egg from every floor.

