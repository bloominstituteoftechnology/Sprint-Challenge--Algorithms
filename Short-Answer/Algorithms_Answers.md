#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(log n)
Since this function just sets a static value to loop toward and then tries to reach it in a relatively efficient way by adding n squared, rather than looping over a range or collection of length n, it looks like log n to me. Also looks like any negative value for n will keep the while loop from executing at all, while n = 0 will run infinitely, since a will stay at 0 and equal n forevermore.

b) O(n log n)
The first linear n comes from the for loop over range(n). The log n comes from the fact that the function loops again toward n, but by doubling j each time through, which cuts down the time in that loop to log n. And then we multiply them together.

c) O(n)
Since this recursive function only calls itself once and moves steadily toward the base case, I believe it shares the complexity of a typical loop through all the elements of a list/array, O(n). I mean, it looks like we could also just do bunnies \* 2, but that's none of my business.

## Exercise II

Like I always say, if you want to find the right floor, you've gotta break a few eggs. My initial plan would be to essentially do a binary search of the floors, runtime complexity O(log n), by starting with the middle floor of the building, or the highest floor // 2. If any egg dropped from there breaks, I know to head halfway down toward ground level and try again. If it survives the drop, I split the difference between the middle floor and the top and try again. So each time I drop an egg I'm cutting the number of floors where f might be found in half. By this method, I should eventually find consecutive floors where the egg does and does not break, and the floor where it breaks is f.
