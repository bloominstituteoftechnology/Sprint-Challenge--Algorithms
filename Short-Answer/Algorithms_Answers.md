#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)a = 0 run time is O(1)
  the while loops runs O(n^3) times since it's going from 0 to n^3.
  the third line a = a + n* n is O(1)

  giving it a runtime of O(n^3)


b)  line 1 = O(1)
    line 2 is O(n)
    line 3 is O(1)
    line 4 is O(n-1) since it's going starting from 1 to n. which is still O(n)
    line 5 and 6 are constants O(1).
    as line 2 - 6 is a set of nested loops, we can ignore the O(1).
    but multiplying O(n) and O(n-1) gives us O(n^2-1) which is O(n^2)

c) as this is a recursive function that only calls itself once per recursion, we can determine the complexity as O(n)


## Exercise II

We can do a divide an conquer for this algorithm.

we have n story.
Our initial base case would be if
n = 0 it returns 0 egg drops. while n= 1 would return 1 egg drop .This first two lines would be a linear run time.

Since if an egg breaks if it's a floor above. we'll need to set n-1 as a test once we find a breaking point. In this scenario going from bottom up will be a good idea.

we can divide n in 10 parts, basically giving a 10% increase so if a floor has 100 floors, the initial test would be 0,10,20, etc per loop.
we'll set the lower = 0
and ten_percent = n/10
test_floor = ten_percent

so what we'll do is
if egg is drop in the test_floor and it doesn't break, we'll move up the next 10 percent and set lower as n/10 and test_floor would be test_floor + ten_percent.

if it breaks in the ten_percent.
we can check we'll check the halfway point between lower and test_floor.
if it breaks in the halfway point, then that means our egg is between that lower and that halfway.

we'll repeat the halfway checks here until we know that egg breaks in test_floor and doesn't break in test_floor -1.

Setting the initial setting will be O(1)

our base case would be if egg breaks in test_floor and doesn't break in test_floor - 1.

for floor test, if it doesn't break, it would be O(n) * O(1)

if it breaks it would be
O(n) * O(n) giving us O(n^2)
