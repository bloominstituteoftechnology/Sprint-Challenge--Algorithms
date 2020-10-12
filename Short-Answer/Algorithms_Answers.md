#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I


a) Linear time: Although we are doing ’n’ cubed in the conditional and squaring it in the loop, the size of ’n’ has no bearing on how the function will scale. We are still doing a constant calculation overall.


b) n log n: The outer loop is going through an ’n’ number of times. And inside the inner while loop ‘j’ is being doubled, so the while loop would finish twice as fast as the value of ’n’. So there is a nested for loop and overall we go with the longest time complexity, which is n log n


c) Linear time: The function calls itself recursively subtracting ‘bunnies’ which is ’n’ and adding 2 to each iteration until n reaches 0. So while the function is a recursive function it only runs ’n’ number of times while adding 2 (which is a constant time complexity)

## Exercise II

This sounds like a great use of using a Binary structure.
	I would find out which floor is in the middle from the top and bottom floor and drop an egg. If the egg breaks I would go to the floor half way between the bottom and my current floor and repeat for every time the egg breaks.
	If the egg doesn’t break for whichever floor I’m testing, I would go half way up from my current floor to the highest floor that I tested last, and repeat. If it broke on my first test, I would go halfway up from the middle floor to the top floor. And repeat the process.

The time complexity of my testing would be a Log N, as I’m cutting the required amount of times I have to drop an egg in half each time.
