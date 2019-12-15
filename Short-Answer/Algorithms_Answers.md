#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

# Exercise 1

a) This will run in O(n) as "a" will calculate as many times as the value of n

b) This will run in O(n logn) as the outer loop will run for every value of n, while the inner while will run in half the iterations due to j reaching the value of n twice as fast.

c) This recursive function will run in O(n). There is a space complexity due to the recursion, but the runtime is still O(n)

# Exercise 2

I would use a divide and conquer method using a Binary Sort approach. I would go to the middle floor and drop an egg from there. If the egg breaks, then I can eliminate any higher floor. If the egg does not break then I can eliminate all lower floors from the midpoint where I am at. I would then continue to go to the midpoint from where I am at, either up or down depending on if the egg breaks or not and continue until I zero in on the lowest floor that the egg breaks. This divide and conquer approach is the best to reduce the number of eggs used to determine the answer. The runtime of this approach is O(logn) since I am reducing the total number of floors I have to test by half each time.
