#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) 
Time complexity O(n). a starts at zero, and increments by n^2 every loop. (n^2)+(n^2)+(n^2)... n times
is equivalent to (n^2)*n = n^3.

b)
Time complexity O(n log<sub>2</sub> n). The outer for-loop is linear time, while the inner for-loop is log<sub>2</sub>
time due to its iterator doubling each iteration.

c)
Time complexity O(n). Each call of the function can only spawn one additional call, and recursion bottoms out once the bunnies
argument decrements to zero, so the number of calls is simply the initial bunnies value.

## Exercise II

If the goal is to minimize the number of dropped AND broken eggs (as in, dropping is fine so long as the egg doesn't break)
then starting from floor 0, and iterating up, dropping an egg at each floor until one finally breaks would be ideal.
This algorithm would have linear runtime, would only ever break one egg, and the floor at which the egg broke would be f.

If the goal is to minimize the number of dropped OR broken eggs (as in, both breaking and just dropping eggs should be minimzed)
a binary search would work very well. The only trouble here is that to know if any given floor is the highest floor eggs can be dropped from, we'll have to check the floor above it. We can't break out early if our middle value happens to luckily be assigned to the correct value - or we *could*, but this would cost us twice as many broken eggs to check each time. This algorithm will have 
log<sub>2</sub>n runtime.


```
def egg_drop(floors -> int):

    bot = 1 
    top = floors
    egg = Egg()

    while top > bot: # this loop runs until convergence
        mid = (bot + top) // 2
        is_broken = egg.drop(mid)

        if is_broken:
            top = mid - 1
        else:
            bot = mid + 1

    # after convergence, drop an egg. If it breaks, that's f. Otherwise f is one floor higher.
    if egg.drop(mid) is True:
        return mid
    else:
        return mid + 1

```
