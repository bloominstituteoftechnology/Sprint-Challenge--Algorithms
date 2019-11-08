#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n)
This is essentially trying to get to n cubed by repeatedly adding n squared, which should take n tries for any given number, so O(n).

b) O(n log(n))
The first n comes from the for loop through range(n); the log(n) comes from the while loop, since j is increasingly exponentially toward n. And then those get multipled together.

c) O(n)
Since this moves recursively toward a base case of bunnies == 0 by subtracting 1 each time, it should run once per bunny, so O(n).

## Exercise II

My plan would be to essentially do a binary search of the building, runtime complexity O(log n), by starting with the middle floor of the building, or the highest floor // 2. If any egg dropped from there breaks, I know to head halfway down toward ground floor and try again, and the floor I dropped the egg from becomes the new "highest floor". If it survives the drop, I split the difference between the floor I'm on (making it the new "ground floor") and the top and try again. So each time I drop an egg I'm cutting the number of floors where f might be found in half based on the result. By this method, I should eventually find consecutive floors where the egg does and does not break, and the floor where it breaks is our f.
