Add your answers to the Algorithms exercises here.

## Exercise I

a) The loop is O(n) because it doesn't really modify `n` hence every loop, `n` just grows in linear time.

O(1) + O(n) = O(n) because O(n) dominates O(1)

```python
a = 0  # O(1)
while (a < n * n * n)  # O(1) * O(n) = O(n)
  a = a + n * n  # O(1)
```

b) O(1) + O(n^4) = O(n^4)

```python
sum = 0  # O(1)
    for (i = 0; i < n; i++)  # O(n) * O(n^3) = O(n^4)
      for (j = i + 1; j < n; j++)  # O(n) * O(n^2) = O(n^3)
        for (k = j + 1; k < n; k++)  # O(n) * O(n) = O(n^2)
          for (l = k + 1; l < 10 + k; l++)  # O(1) * O(n) = O(n)
            sum++  # O(1)
```

c) O(2) + O(n) = O(2n) = O(n) This recursive function is just like looping through each bunny. It terminates when `bunnies == 0` and then counts back how many are the total bunny ears. That's why the recursive calls are considered O(n).

```javascript
bunnyEars = function(bunnies) {
  if (bunnies == 0) return 0;
  return 2 + bunnyEars(bunnies - 1);
};
```

## Exercise II
