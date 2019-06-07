# Exercise 1

```
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

| n | steps |
| --- | --- |
| 0 | 0 |
| 1 | 1 |
| 2 | 3 |
| 3 | 4 |
| 4 | 6 |
| 5 | 7 |

$$\begin{cases} a_n = a_{n-1} + 1,& \text{if } n \text{ is odd}\\a_n = a_{n-1} + 2,& \text{otherwise} \end{cases}$$

$$\text{steps}(n) = \begin{cases} \frac{3}{2} * (n - 1) + 1,& \text{if } n \text{ is odd} \\ \frac{3}{2} * n,& \text{otherwise} \end{cases}$$

$$O(n)$$

```
b)  sum = 0
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

| n | steps |
| --- | --- |
| 0 | 0 |
| 1 | 0 |
| 2 | 0 |
| 3 | 0 |
| 4 | 0 |
| 5 | 9 |
| 6 | 36 |
| 7 | 90 |
| 8 | 180 |
| 9 | 315 |
| 10 | 504 |

$$a_0 = a_1 = a_2 = a_3 = a_4 = 0\\a_n = a_{n-1} + \frac{9}{2} * (n - 3) * (n - 4)$$

$$\text{steps}(n) = \frac{3}{2} * (n - 2) * (n - 3) * (n - 4) = \frac{3}{2}n^3 - \frac{27}{2}n^2 + 39n - 36$$

$$O(n^3)$$

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

| n | steps |
| --- | --- |
| 0 | 0 |
| 1 | 2 |
| 2 | 4 |
| 3 | 6 |
| 4 | 8 |
| 5 | 10 |

$$a_0 = 0\\a_n = a_{n-1} + 2$$

$$\text{steps}(n) = 2 * n$$

$$O(n)$$

# Exercise 2

```
# Minimum and maximum floor drop height
l = 0
h = n + 1

# Run through loop
while True:
    # Test to find if at answer, if so, break loop
    if h - l == 1:
        break

    # Set test floor to int average of highest and lowest floor
    f = (h + l) // 2

    # Drop egg and see if it breaks at floor f
    # This could be replaced with `if f >= true_f:`
    if drop(f):
        # If it does break, repeat in loop for bottom half of floors by setting maximum to f
        h = f

    else:
        # If it doesn't break, repeat in loop for top half of floors by setting minimum to f
        l = f

# Return output of broken loop
return (h + l) // 2
```

| n | max_steps |
| --- | --- |
| 1 | 1 |
| 2 | 2 |
| 3 | 2 |
| 4 | 3 |
| 5 | 3 |
| 6 | 3 |
| 7 | 3 |
| 8 | 4 |
| 9 | 4 |
| 10 | 4 |
| ... | ... |
| 128 | 8 |
| 256 | 9 |
| 512 | 10 |
| 1024 | 11 |

$$\text{max\_steps}(n) = \lfloor \log_2{n} + 1 \rfloor$$
$$O(log(n))$$

The runtime complexity of the pseudo-code is $O(log(n))$, as this pseudo-code is techically a binary search and with large values of $n$ the runtime complexity of the code will be much smaller than runtime complexity $O(n)$.
