#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n). I would say this because as n increases, the number of operations scales linearly. If n = 2, the while loop will run 2 times. If n = 5, the while loop will run 5 times, and so on.


b) O(n log n). This one is tricky. I say it's O(n log n) because I broke it into two parts. The first for loop, we are iterating through all of n, so that would be O(n). For the while loop, as n increases, the number of operations increases, but not linearlly. For n = 5-8, the while loop runs three times, for n = 9-16, the while loop runs 4 times. Thus the operations are increaing, but at a slower rate than O(n). So this would be log n. O(n) * O(log n) gives you O(n log n). You can also keep an eye on the sum counter. As n goes up, the sum is larger than n, but smaller than n^2. And what's in between O(n) and O(n^2)? O(n log n).


c) O(n). This works similar to the factorial problem I think. Whatever your n is, you recur n times (because base case is bunnies == 0 and not bunnies == 1). So you are always going to have the one base case operation, plus n recursions. O(1 + n)When approaching infinity, that 1 is absolete so it becomes o(n).

## Exercise II

I would run it like a binary search problem to find floor f. You first go to the middle floor. Assuming ground floor is 0, and you have a 6 story building, start in the middle on the 3rd floor. Throw off an egg. If it cracks, you know you are higher than floor f. Let's say it cracks. Then you would assume floor 2 in the top of the building, and floor 0 is still the bottom. The middle floor at that point is now floor 1. You throw it off and it doesn't crack, you know floor 2 is floor f. If it does crack, floor 1 or floor 0 could be floor f so you would need to try tossing an egg one more time. The runtime complexity would be O(log n).

In general with binary search. Here's how the code would work:

```python
def binary_search(building(an array)):

    # start with low floor at 0
    low_floor = 0
    # and high floor at the last floor in the array
    high_floor = len(arr) - 1

    if middle_floor == high_floor:
        middle_floor = high_floor = floor f
    
    while low_floor < high_floor:
        
        # add low and high, divide, and round down to get the middle
        #. floor.
        middle_floor = (low_floor + high_floor) // 2

        # Throw an egg
        
        # if the egg cracks, for the next loop we can make
        #. the high floor one less than the last middle
        if egg cracks:
            high_floor = middle_floor - 1
            
        # if the egg doesn't crack, for the next loop we can make the low floor
        #. one more than the last middle
        if egg doesn't crack:
            low_floor = middle_floor + 1
            
        # keep going until there's just 1 floor left, and that's your f floor
```