#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n): Whatever the value of n is will increase the runtime for the while loop. Making it type linear runtime.


b) O(n log(n)): The for loop is O(n) because it depends on what the value of n is making it a type of linear runtime. The while loop inside the scope is O(log n) becuase the index (j) is being multiplied by two, everytime the loop is ran. Thus, the whole algorithm is O(n log(n)).


c) O(n): Just the values of bunnies is being reduced by one everytime recursion occurs. Making it type linear runtime.

## Exercise II

# Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

# Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

Binary tree algorithm would be useful in this situation. That would allow us to search through the floors to see if we can drop the egg from a higher floor. Or if we need to go lower if it breaks.

The first floor would be equal to 0, the middle floor would be equal to the (first floor + top floor) // 2, and the top floor would be equal to the length of floors (len(f)).

If we drop the egg from the middle floor first we can then see if the egg breaks. If so, we know we will have to go lower (f - 1). If not, we kmpw we will have to go higher (f + 1).

This algorithm would use O(log n) since we are eliminating half of the floors based on the input of floors (f).




