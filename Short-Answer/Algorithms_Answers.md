Add your answers to the Algorithms exercises here.
a) a = 0
while (a < n _ n _ n):
a = a + n \* n

      n=1 Will run once
      n=2 Will run twice
      n=3 Will run three times
      0(n)

b) There are 4 nested loops 0(n^4)

c) O(N) as it is a recursive function

I would apprach this problem in a similar way to finding a word in a dictionary, that is to use a recursive algorithim (binary serach) to half the number of floors until the correct floor is found.

For an n story building, in order to found floor f, I would drop the egg off of floor n/2

If the egg breaks, floor n/2 becomes the top floor and I would take n/2 until the correct floor is found

If the egg did not break on the initial drop, n/2 would become the buttom floor and would do n/2 again until the number of floors is reduced to find floor F.

O(n)
