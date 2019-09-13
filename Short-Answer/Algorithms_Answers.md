Add your answers to the Algorithms exercises here.

## Exercise I

a) runtime = (n * n * n)/(n * n) = n
this algorithm has a runtime of 0(n)

b) runtime = n * n * n * 10
this algorithm has a runtime of 0(n**3)

c) this algorithm has a runtime of 0(n)

## Exercise II

We make floor an array of 0s and 1s, 0 being the egg does not break, and 1 being the egg does break;
e.g. floor = [0, 0, 0, 0, 1, 1, 1, 1, 1]
 --There are 9 floors (n = 9), and the egg starts breaking on the 5th floor.

```python 
def find_f(floor):
    low = 0
    high = len(floor)  - 1
    while low < high:
        mid = (low + high) / 2
        if floor[mid] == 1:
            if floor[mid-1]== 0:
                return mid
            else:
                high = mid - 1
        elif floor[mid] == 0:
            if floor[mid+1] == 1:
                return mid + 1
            else:
                low = mid +1
```
The runtime is 0(2*lg(n))

