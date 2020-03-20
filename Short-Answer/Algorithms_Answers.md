#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

```python
a = 0
while (a < n * n * n):
	a = a + n * n
```

a) O(n) - it will take n iterations precisely.

```python
sum = 0
for i in range(n):
	j = 1
	while j < n:
		j *= 2
		sum += 1
```

b) O(n*log(n)) - The outer loop is O(n), while the inner loop is O(log(n))

```python
def bunnyEars(bunnies):
	if bunnies == 0:
		return 0

	return 2 + bunnyEars(bunnies-1)
```

c) O(n) - This is just a O(n) loop in recursive form.

## Exercise II

```python
def check_break_height(floors):
	if egg_breaks(floors // 2):
		return check_break_height(floors // 2) + floors // 2
	else:
		return check_break_height(floors // 2)
```

This should determine break height in O(log(n)).

