# Analysis of Algorithms

## Exercise I

a) O(n)

```python
  a = 0
  a = n^2
  a = 2n^2
  a = 3n^2
  ...
  a = nn^2
```

b) O(n^3)

```python
# O(n^3)
for i in range(n):
  i += 1
  # O(n)
  for j in range(i + 1, n):
    j += 1
    # O(n)
    for k in range(j + 1, n):
      k += 1
      # O(1)
      for l in range(k + 1, 10 + k):
        l += 1
        sum += 1
```

c) O(n)

`bunnies` decrements by 1 each time the function recurses.

## Exercise II

Looks like we'd want to start in the middle. Then we'd drop from the middle of the top half if the egg doesn't break, or the bottom half if the egg does break. This feels like a binary search to me, so it'd have a time complexity of O(log n).
