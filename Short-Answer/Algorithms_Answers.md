#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)

```python
 a = 0                   # O(1)
while (a < n _ n _ n):   # 0(n^3)
a = a + n                #O(1)

```

Runtime Complexity: O(n^3)

b)

```
sum = 0                 #O(1)
for i in range(n):      #(n)
    j = 1               #O(1)
    while j < n:        #O(n)
        j *= 2          #O(1)
        sum             #O(1)
```
Runtime Complexity: O(n^2)

c)


```
c)  def bunnyEars(bunnies):
      if bunnies == 0:                     O(1)
        return 0                           O(1)

      return 2 + bunnyEars(bunnies-1)      O(n)

Runtime Complexity: O(n)

## Exercise II



#Like a merge sort algoritm - divide the numbers of floors to and find if the eggs break

- Find out the first flor ( 0 ) and the last floor (high its total number of floors)   
- FIrst check it will be - if first loor smaller that total number of floor            
- Find the flor in the middle and drop the egg
- If the egg break , remove all the floors above
- Find the middle in the first part
- If the floor doesn't break,I will eliminate all the floors below and set the low to middle
- Repet the process until we find the middle flore when egg not breaks (when middle = floor)

- It will be a recursive algorithm (divide and conquer ) with a runtime complexity of O(log(n))



