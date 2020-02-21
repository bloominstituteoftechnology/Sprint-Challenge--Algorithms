#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

The expression inside brackets on L10 is O(1).
L11 is O(1).

The while loop is going to be O(n). The number of loops will increase as n increases.

Final Runtime Evaluation: O(n)

b)
I think this one is O(n^2) because it has a nested loop.

Final Runtime Evaluation: O(n^2)

c)
the recursive call is O(n).
Everything else is O(1).

Final Runtime Evaluation: O(n)

## Exercise II
I would represent the floors of the building as a sorted array. 
So I would create an array.

n = 10
floors = [x for x in range(1,n + 1)]

then , starting on the middle floor I would throw an egg out.

If the egg broke that would mean I was up too high I would go to the floor that was between the bottom floor and the current floor and try it again.

If the egg did not break I would store that floor number in a variable.

not_broken = 5

then I would find the floor that was in the middle of the range between the current floor +1 and the top floor.
I would throw an egg.
 
 If it broke it would mean I had found the highest floor to throw an egg from.

 Otherwise i would update the not_broken variable and repeat.
