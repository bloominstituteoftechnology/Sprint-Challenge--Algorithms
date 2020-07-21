#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(1)
# O(n) -- would run 10 times before while loop breaks

b) O(n)
# O(nlogn)

c) O(logn)
# O(n) -- function runs ten times

## Exercise II

we can implement a binary search for this.

We can start at the midpoint of how high the builing is.

If building is f floors high, we will take midpoint f//2

if the egg breaks at the midpoint, we will obviously need to drop it at a lower height. This means the new max will be midpoint -1.

However, if the egg does not break, we can find the new maximum height. We do this by calculating the new midpoint, and dropping the egg.

we then calculate the new midpoint, then drop the egg. if it breaks there, we can again eliminate the floors above the midpoint. (same logic as above)


This runtime complexity closely matches O(logn)


