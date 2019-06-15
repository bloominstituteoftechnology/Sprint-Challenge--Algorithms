Add your answers to the Algorithms exercises here.

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```
a)  a = 0                       1
    while (a < n * n * n):      n
      a = a + n * n             1
```

Explanation:
I am having trouble with this one. I could see the answer being O(n) or O(n^3). If we break it down line by line, line 1 and 3 are happening 1 time no matter what n is, but line 2 will happen n^3 times. This would give O(1) + O(n^3) \* O(1), which simplifies to O(n^3)... But if we look close and see how a change in n will impact the entire algorithm, we see that inside the while loop, a is increasing at n^2, which will reduce the runtime. This would mean line 2 is increasing by n^3, but line 3 is increasing a by n^2, giving us a difference of n. That would give us O(n).

Official ANSWER: O(n)

```
b)  sum = 0                                 1
    for i in range(n):                      n
      i += 1                                1
      for j in range(i + 1, n):             n
        j += 1                              1
        for k in range(j + 1, n):           n
          k += 1                            1
          for l in range(k + 1, 10 + k):    1
            l += 1                          1
            sum += 1                        1
```

ANSWER: O(n^3)

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:                  1
        return 0

      return 2 + bunnyEars(bunnies-1)   n
```

ANSWER: O(n)

## Exercise II

Suppose that you have an _n_-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get broken if dropped off a floor less than floor _f_. Devise a strategy to determine the value of _f_ such that the number of dropped eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode and give the runtime complexity of your solution.

SOLUTION:
I would have liked to implement an algorithm similar to a binary search to find the highest floor that an egg could be dropped from without breaking. That would have a O(log n) runtime complexity. In the interest of time, I will write out psuedocode for a O(n) algorithm:

def maxSafeFloor(n)
dropfloor = 1
broken = false

    While (broken == false AND dropfloor <= n):
        drop egg from dropfloor
        if egg breaks:
            broken = true
        else:
            dropfloor =+ 1

    if dropfloor == 1
        return 0
    elif dropfloor > n:
        return 'Egg never broke'
    else:
        return dropfloor
