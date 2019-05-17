Add your answers to the Algorithms exercises here.

## Exercise I

(a) O(n) - This operation scales at O(n)

For purposes of calculating the time complexity, following code can be simplified from:
```python
a = 0
while (a < n * n * n):
    a = a + n * n
```
to:
```python
a = 0
while (a < n):
    a = a + 1
```
We can do this by dividing both terms that contain n by n^2. Now we have a formula the looks pretty clear. What we are doing here is adding 1 to a until it in greater than n. This means that our problem scales O(n)

This can be verified, using python's time library, by the fact that for large values of n, say in the millions, the computation time to complete the tasks scales by about 10x for a 10x increase in n. In fact, it scales O(n) at all points in n, it's just very difficult to perceive the scaling behavior for small values of n.

``` python
a = 0
while (a < n * n * n):
    a = a + n * n
```

(b) O(n^3) - This operation scales at O(n^3) (see operation below)
```python
sum = 0
for i in range(n):
    i += 1
    for j in range(i + 1, n):
    j += 1
    for k in range(j + 1, n):
        k += 1
        for l in range(k + 1, 10 + k):
        l += 1
        sum += 1

```
Each for loop (except the last) is a key operation that itself scales at O(n). The nested combination of the first 3 for loops and a multiplicative effect on the scaling behavior, as in O(n) * O(n) * O(n) = O(n^3).

Interestingly, the last for loop is actually just an O(1) operation. Why? Well, the range for l is `range(k+1, 10 + k)`, i.e., it does not depend on n. In fact, we know that this for loop with will only ever loop 9 times, for all values of n.

(c) O(n)
``` python
def bunnyEars(bunnies):
    if bunnies == 0:
    return 0

    return 2 + bunnyEars(bunnies-1)
```
This scales at O(n) because the key operation.



## Exercise II

In order to preserve eggs, I'm going to start from the bottom up (first floor) and drop eggs until I reach a floor _f_ in which, when I drop from that floor, the egg breaks. If the tests are _perfect_, I will only lose one egg maximum using this method.

Pseudocode:


Set a value for whether an egg has broken
start on the first floor

while the egg has not broken:
    drop the egg
    if egg broke, remember that the egg broke
    if the egg didn't break, go up another floor

This algorithm scales at O(n). For each increase in the floor height at which an egg will break, it only takes one more key operation (loop) to check.