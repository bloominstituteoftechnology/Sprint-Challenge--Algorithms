Add your answers to the Algorithms exercises here.

a.To me this looks like it's O(n)

b. We have four nested loops, with the first 3 scaling at n while the last one doesn't take n into consideration.
my guess is O(n^3)

c. This one looks to be O(n)


A brute-force approach might be to just start dropping eggs at the lowest floor and keep going up to find the floor from where the egg will break. This will have a runtime of O(n) as the number of operations will increase by each floor as we go up.
Another approach might be to do a binary search here since we can assume that our floors are sorted like numbers would be in an array. We can divide the floors in half and drop an egg from the middle floor. If the egg doesn't crack, we have to keep going up. If it cracks, we know we're too high and we go down a floor.