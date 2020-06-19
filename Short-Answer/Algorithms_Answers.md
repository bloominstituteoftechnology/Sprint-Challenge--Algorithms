#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Runtime comp - O(n) - Single step linear increase .


b) Runtime comp - O(n) - Seems like there is a second loop but second loop is a comparison and not an iteration .


c) Runtime comp - O(1) - Despite recursion , constant is returned and none is being looped over

## Exercise II

Would use BST method here;

    Drop egg from middle:
        if egg broke:
            current floor - 1
        elif egg != broke:
            current floor + 1 until egg = broke

Runtime comp would be O(log n)
