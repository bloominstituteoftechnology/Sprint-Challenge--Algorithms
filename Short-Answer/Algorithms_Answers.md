Add your answers to the Algorithms exercises here.

Ex 1a)

O(n)
The While loop will run n time to let n^2 excess n^3

Ex 1b)

O(n^3)
The i, j, k loop will have a O(n) and the l loop will have a O(1). Becasue it is a nested loop
We mulitply the running time together.

Ex 1c)
O(n)
The recurive function reduce n by 1 each time until it reach 0. It will take n step.

Ex 2)

Steps:
Let the level we are dropping the egg be x 
assign n/2 to x
Let min, and max be the minimum and maxinum possible outcome of f
Initial min be 0 and max be n
1. Start with dropping the egg from the x level
2. Check if the the egg is broken or not
3. If it is broken, f will be between min and x. Then
    assign x to max
4. If it is not broken f will be between x to max. Then assign x to min
5. Assign (max - min) /2 to x
6. Repeat step 1 until max-min=1, f will equal to max.


The runtime complexity will be O(log n )
