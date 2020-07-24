#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) I think the runtime would be O(n) because it does run more times as n, the input set, gets larger - but it does not get logarithmically or exponentially larger.


b) The runtime would be O(n ^ 2) because of the two loops. The for loop will be O(n) because it linearly increass in time with respect to the input. The while loop also would be O(n), so the combination of O(n*n) results in O(n^2)


c) O(n), the second part increase linearly with the size of 'bunnies' and the first part is O(1)

## Exercise II

I would use a method such as binary searching and start with the middle floor to check if the egg will break or not. If it does not, I will move to the midpoint floor of the higher half of floors, and if it does I will move to the midpoint floor of the lower half. Then I will continue this until the highest floor where the egg doesn't break is found. 

I think the complexity for this will be O(log2n) based on the typical complexity for the binary search algorithm.  