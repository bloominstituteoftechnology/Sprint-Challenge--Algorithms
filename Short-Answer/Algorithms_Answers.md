#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime complexity is O(n). This is because a is equal to n * n, and the while loop only runs on a single additional * n

b) The runtime complexity is O(n^2). This is because we enter a loop inside of a loop that are both n based. So we will have to run over n * n

c) The runtime complexity is O(n). This is because each time the function will return 1 less than it was before, so we will only run as many times as we were initially given

## Exercise II
Say we are using a Binary Search Tree

We will drop on the floor equal to half of building height n // 2

If the egg breaks, we insert {f: false} to the right of the tree, f being the floor and false being survival of the egg. Then we run again from floor f // 2

If the egg does not break, we insert {f: true} to the left of the tree, f being the floor and true being survival of the egg. Then we run from (n + f) // 2 meaning half of the point between middle and top

we repeat this process until the BST's get_max ( on condition that the egg survived ) returns true and also the BST's contains method returns true for a value 1 higher than the max.

