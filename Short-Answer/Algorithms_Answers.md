#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) **O(n)**
n^2 can be factored out of the 'while' condition and the looped expression, meaning it would simply take n steps to escape the loop.
Example 1: n=10; while a < 1000; loop1, a=100; loop2, a=200; etc; 10 (or n) steps to escape
Example 2: n=100; while a < 1,000,000; loop 1, a=10,000; loop2, a=20,000; etc; 100 steps (or n) to escape

b) **O(nlogn)**
The sum is superfluous, as it is not used as a condition. It can be ignored.
The outer loop will run n times. Within that, the inner 'while' loop will run logn times. Every time through the loop, j (which is inversely related to the loop complexity) is doubled. As j rises exponentially, the complexity becomes logarithmic.
Hence, the every outer loop of complexity O(n) has an inner loop of complexity O(logn), and we multiply them to get our answer of O(nlogn)

c) **O(n)**
This is essentially equal to a simple for-loop in time complexity. It starts at f(n), and recursively computes f(n-1). Each function call has only one recursive call, so it becomes like one for-loop. f(n) will have made n recursive calls once it's complete.

## Exercise II
```
Strategy: Use a "binary-search"-like algorithm to cut the number of floors to test in half with each egg-drop-test

def find_highest_floor(n):
    low = 0
    high = n

    test_floor = n / 2

    while test_floor != (high - 1): #**
        test_floor = (low+high) / 2
        if tossed_egg(test_floor) is broken:
            high = test_floor
        else:
            low = test_floor
        # test next floor
    return test_floor

#**: we want the highest possible floor, so we want the next lowest floor than one that breaks the egg

runtime: O(logn)
```
