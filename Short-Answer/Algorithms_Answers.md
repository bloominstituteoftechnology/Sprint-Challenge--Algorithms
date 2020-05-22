#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) Runtime: 0(n^3)
The amount of times that the code runs is determined by how many times the while loop will run. n^3 is the equivalent of n*n*n. As the value of n increases, the result will grow as well.

b) Runtime: O(n log n)
The inner loop will increase linerally as the value of n increases. However, the inner loop has a runtime of 0(n) because as the value of j gets doubled, n's value is getting halved.

c) Runtime: 0(n)
The amount of times the code gets run is determined by the amount of bunnies added to the function.

## Exercise II

0 is the lowest point you can drop an egg from because it is the lowest possible integer and there is no constraint on f, allowing for that value to be maximized. The time complexity could be 0(1) as the algorithm will not change based on the size of the input (f)

The first function could take a parameter that determines the floor value (input -> f). Within the function there will be a conditional statement for dropping an egg. It could be flow something like --> drop the egg, conditional statement --> if egg breaks --> return true --> else --> return false.

The second function could then take f --> set it to 0 --> loop over a conditional statement --> drop an egg from the current f value --> if it doesn't break ---> increment f by 1 and repeat --> else: return f - 1
