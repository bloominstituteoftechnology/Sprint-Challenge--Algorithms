#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    Run-time: O(n)
    Justification: With every runtime of the algorithm, a gets incremented by n*n until it eventually reaches n * (n * n). To use an example, if n = 3, after the first loop, a would be 9 (n * n = 3 * 3). After the second, it would be 18 (a + n * n = 9 + 3 * 3). And after the third, we'd reach our answer of 27 (a + n * n = 18 + 3 * 3. This is the same as 3 * 3 * 3)


b) 
    Run-time: O(log(n))
    Justification: Due to j being doubled after every single iteration, our runtime increases by 1 every time our dataset doubles. Therefore, when passed n = 32, sum will be 6, whereas it'll be 7 when passed 64. Ergo, it's a super efficient algorithm.


c)
    Run-time: O(n)
    Justification: While at first glance this problem looks like O(1), since it only does a single operation when bunnies equals 0, I nevertheless think that this particular algorithm has a runtime-complexity of O(n) since it requires one additional function call for every value in bunnies. Space-efficiency notwithstanding.

## Exercise II
    CONSTRAINTS:
        - Building has n floors.
        - Unlimited eggs.
        - If floor >= f   --> SPLAT!
        - else            --> YAY!

        - Goal is to minimize the number of broken eggs
        - Seems like a classic case of binary search

    PLAIN ENGLISH: First, go to floor n/2, the very middle of the building. Then, you drop an egg. If you hear SPLAT! from down below, you the move halfway down the tower (halfway between the current floor and the bottom). Then you try again. If you'd heard YAY! from the bottom of the tower, you'd move halfway up the tower (halfway between the current floor and the top). Then you'd try again. You'd do this over and over, moving slightly up or down the tower (every time halfway between your current location and the number of floors you hadn't tried yet). In doing so, you whittle down half the potential options with every go until you eventually figure out the exact floor where dropping the egg doesn't break it and dropping it from the floor above does.

    PSEUDOCODE:
    Function
        Move to n//2

            if the range of possible floors is 1:
                return that value

            Drop egg
            
            If egg is broken:
                rerun function with range of possible floors with  n//2 as the lower bound

            if egg is fine:
                rerun function with range of possible floors with n//2 as the upper bound


    RUNTIME: O(log(n))
