#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
     a = 0
    while (a < n * n * n):
      a = a + n * n

The runtime here is O(n).
There is a single while loop, which will perform more linear operations the larger n is.

b)
    sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1

The runtime here is O(n^2).
There are two loops being used here. It starts with a for loop which contains a while loop.

c)
    def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

The runtime here is O(n)
This one is using recursion. Each call will perform an if check.

## Exercise II

"Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized."

So this problem seems to be asking how to determine the value of f as soon as possible so that I don't lose too many
eggs. In this case, I would start by dropping the egg on the median floor and see if it breaks. If it does, then I
would take the halfway point between the first floor and the median and drop the egg there to once again see if it breaks. So pretty much, I would keep checking halves until I've pinpointed the last floor that the egg can survive from if it was dropped. The runtime of this would look something like O(n*n).