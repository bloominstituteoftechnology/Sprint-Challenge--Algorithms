Add your answers to the Algorithms exercises here.

## Exercise I

```
a)	The run time of the following code snippet is Linear O(n):

	a = 0
	while (a < n * n * n):
		a = a + n * n

It is linear because the number of operations scales directly with the size of the data.
```

```
b)	The run time of the following code snippet is Exponential O(2^n):

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

It is exponential because the number of nested loops increases as a function of the input size. 
```

```
c)	The run time of the following code snippet is Quadratic O(n^2):

	def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

It is quadratice because the differences have a constant difference and it is a recurssive function.
```

## Exercise II

```
I have a building with n number of stories. If I throw and egg out the window from a floor f or higher if will break, otherwise it will not break. I need to devise a strategy to find the floor while dropping the smallest number of eggs.

My strategy would be to use binary search in order to test floors.

def find_break_point(n):
	
	midpoint = len(n) / 2	

	for f in range(int(midpoint), len(n)):

		if n[f] == "broken":
			if n[f-1] != "broken":
				return f + 1
			else:
				return find_break_point(n) - midpoint

		elif n[f] != "broken":
			if n[f+1] == "broken":
				return f+1 + 1
			else:
				return find_break_point(n) - midpoint

My solution is Quadratic O(n^2) because it is recurrsive and slopes up quickly.
```
