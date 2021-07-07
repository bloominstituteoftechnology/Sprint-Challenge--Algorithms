#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  O(n)
    The function is just multiplying n,
    not running through it n times
    Originally thought O(n^5), but now I don't think it's actually that complex


b)  O(n^2)
    The for loop is O(n) because it will increase in size linearly with n. The while loop is also O(n),
    since they both need to run through it's O(n * n) or O(n^2)


c)  O(n)

    First part of the function will is O(1) bc it always execute in the same time/space, no matter the size of bunnies, but the second part iterating over (bunnies -1 ) is O(n), so the whole function is

## Exercise II

At first was thinking about minimizing broken eggs by starting at floor 1 and moving higher until until an egg is broken, based on common sense that an egg will break when dropped from a low floor.

But in this example, perhaps an egg can withstand higher falls than the real world.

So I would do a Binary Sort to split n-stories at the median, drop an egg, then repeat until you find the the highest floor f where the egg does not break.

The complexity for this algorithm would be O(n).
