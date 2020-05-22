#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

 O(n), time to run is proportionate to size of n

b)

 O(n^2), time to run is prportionate to size of n _ n, because we loop through it twice one for range(len(n)) and once when j < n j _ 2, morover O(n \* (n/2) -> O(n^2)

c)

O(bunnies), recursive function call for each item in bunnies O(n)

## Exercise II

n floors in a building, find floor f (where arbitrary eggs don't arbitrarily break)

create a binary search tree from list of n floors of a building

check if dropping an egg from each leftern node causes the egg to break

if it causes an egg to break continue to left node

when the egg does not break continue right node, then left etc..

when the egg breaks on a node save and return that value

- the runtime is O(log(n)) at a minimum or O(n) at a maximum, depending on which floor the egg breaks. For example; If the egg breaks on the highest floor of the building the runtime is O(n) because we have to traverse the entire tree before we return a value.