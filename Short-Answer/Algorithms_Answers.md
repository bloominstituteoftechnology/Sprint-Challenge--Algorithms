#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)


b) 0(n^2) because performance is directly proportional to the square of the size of the input data set and there is a inner while loop nested in a outer loop. ( so if it was cubed then it would be 0(n^3) )


c) This is an example of 0(n) because recursion is being used and will run till its over. When you increase the input the longer the input. A cache would be helpful!

## Exercise II

--First we want to understand whats going on.--

    it will have 2 params (egg, floor)

    building n floor F or higher will break the egg if dropped or else it wont break

    If I am on the ground floor then no eggs will break

--merge sort or binary search--

    I would go with binary search since the number of floors should already be in order.

So to find the highest floor where the egg does not break i would divide n(floors) in half and dropping the egg from the middle floor.

    if it broke from the middle floor then i would not have to test the higher floors and then repeat the same process one step above on the smaller floors from above^

    if it did NOT break from the middle floor that would let me know I dont have to test the lower floors and to repeat the same process of dividing the upper half .

So each time im getting rid of one half of the floors until i get to the golden egg room that does not break from falling from n story in building!

0(n) since we dont know how often it would loop


