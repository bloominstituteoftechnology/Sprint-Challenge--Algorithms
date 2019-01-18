Add your answers to the Algorithms exercises here.

a. The runtime of this algorithm is O(n). The n value stays the same while the variable increases at a linear pace. For example, with an n of 2:

a = 0
    while (a < n * n * n) 
      a = a + n * n

In this case our (n * n * n) is 8, so our a would increase like so:
(n * n) = 4

a = a + (4) = 4
4 = 4 + 4 = 8
8 = 8 + 4 = 12
12 = 12 + 4 = 16

etc.

Our data here gives a linear curve since a is increasing at a constant pace, so the runtime is O(n).

b. Here we have a total of 4 loops which count to n, so the best we are going to be able to do is O(n ^ 4) runtime.

for (i = 0; i < n; i++)
      for (j = i + 1; j < n; j++)
        for (k = j + 1; k < n; k++)
          for (l = k + 1; l < 10 + k; l++)

The fourth loop initially looks as though it is separate from n, which would factor into our consideration of this runtime. However, in the previous loop we've established that k is also approaching n, so our values in the fourth loop are going to follow suit and give us O(n ^ 4) in total.

c. The most important thing to note here is that bunnyEars is recursive so the runtime consideration needs only to account for the basic functionality of the algorithm, which is this line:

 return 2 + bunnyEars(bunnies-1)

Since all we're doing here is returning a value and then decreasing "bunnies" by 1, we're looking at a basic linear relationship. Whatever our "bunnies" value is, we return a new value for each line until that count hits 0 and the return also becomes 0.

This linear relationship indicates another O(n) runtime.

Eggsercise II

This can be viewed essentially as a binary search algorithm. The best guess we could make on the first turn for minimizing the number of eggs dropped would be an n // 2 guess, meaning we would go to the halfway point up the building and drop our first egg. Two cases arise from this:

n >= f, the egg breaks. We go halfway down from our current (n // 2) floor.
n < f, the egg does not break. We go up halfway between our current floor and n.

We simply repeat these steps for every egg drop based on the result. Drop the egg, find the appropriate halfway point up or down, and drop another egg. This way we make the most efficient guess each time.