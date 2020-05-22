#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) The result of the input increases as a constant of the input. 


b) O(n^2) The while loop functions like a for loop. There are two nested operations. The performance is the square of the input data.


c) O(n) As a recursive function, input is subtracted by 1 and added with 2 uniformly. It is O(n) because the runtime will increase at a constant pace with the size of the input.

## Exercise II

# Analysis of Algorithms

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

Psuedocode:
```
# for n number of floors
# instantiate a range that we save for each iteration [min, max]
# 1 . find random floor x between lowest floor,  min and highest floor, max
# 2 . if n is less than f:
# 3 . n does not get broken, store this number, next time iterate through smaller f by assigning x as max
# 4 . else n gets broken
# if n is broken, find random floors again repeating steps 1-4, assign x as min
```

Complexity is O(log n) because this is a search problem, which is T(n)=1+1/2+1/3+...+1/n

