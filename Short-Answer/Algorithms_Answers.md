#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
This functions represents a polynomial runtime, or O(n^c). The reason is that although the inner functions looks to reduce the number of operations, it is apperant the outer while loop will have a greater effect of increasing the operations. I believe the full runtime equation would look something like O(n) = n^3 - (n^2 + a). Which reduces to just O(n^3)

b)
This function represents a loglinear runtime, or O(n log n). Here, the outer function and inner function both add to the runtime. Although the inner function does so with a significant reduction in magnitude O(log n), it has to do that work for every instance of n.  

c)
This function represents a linear runtime, or O(n). While going through each recursive call to the base case, each call is only operated on once, which means there are only n operations. 


## Exercise II
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized

A naive approach to findind f would be to start by throwing an egg from the first floor, checking if it broke, and then increment to the second floor. Continue doing this, increasing the floor you throw from each time, until your reach a floor where the egg does finally break. This approach works and would be good up to a certain point, but at its worse, you would had to have gone through all the floors and dropped a lot of eggs if they don't break until the nth floor. A better approach would be starting on the middle floor to see if the egg breaks. If it does, go up to the next midpoint of the remaining floors above you and try again. If it doesnt, for to the next midpoint below and try. Kept repeating until you find the floor that the egg breaks. This would allow you to cut the number of eggs you throw out by a good amount. I would say at worse, you would throw out O(log n) eggs. 


def egg_dropper(n):
    start = 0
    end = len(n)
    egg_breaks_floor = random.random(n) #find a random number from 1 to n (i think)

    while start < end:
        middle_floor =  (start - end) // 2

        if middle_floor == egg_breaks_floor:
            return middle_floor
        elif middle_floor < egg_breaks_floor:
            start = middle_floor + 1
        else:
            end = middle_floor - 1
    
    return -1

