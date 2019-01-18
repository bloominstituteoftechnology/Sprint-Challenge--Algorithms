Add your answers to the Algorithms exercises here.
```
1a) a = 0
    while (a < n * n * n) 
      a = a + n * n
```
There is one loop which has a time complexity of O(n). You multiply the nested time complexities to get O(1) * O(n) = O(n). O(n) dominates the O(1) (from a = O); O(n) would be the time complexity of the entire code. 

```
1b) sum = 0   O(1)
    for (i = 0; i < n; i++)    O(n)   
      for (j = i + 1; j < n; j++)    O(n)
        for (k = j + 1; k < n; k++)      O(n)
          for (l = k + 1; l < 10 + k; l++)  O(n)
            sum++    O(1)
```
For all of the nested for loops you multiply their time complexities to get O(n) * O(n) * O(n) * O(n) * O(1) = O(n^4). This dominates O(1) from the first line, O(n^4) becomes the overall time complexity.


```
1c)  def bunnieEars(bunnies)
      if bunnies == 0:
        return 0

      return 2 + bunnieEars(bunnies-1)
```

This function calls itself so the time complexity is O(n).


2. _n_-story building and plenty of eggs
  egg breaks  if floor _f_ or higher
  doesn't get broken if dropped off a floor less than floor _f_.
  determine the value of _f_ number of dropped eggs is minimized.

  Use binary search to find the value of f
  def break_eggs(n, current_floor):
    if current_floor >= f:
      print("eggs break")
      current_floor = f//2
    else:
      print("eggs don't break")
      return current_floor

The time complexity would be O(log(n)) because we are cutting the searches to find the value of f in half every time by diving it by 2.