#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)


b) O(n^2)


c) O(n)

## Exercise II

the variable 'building' represents the building.
the variable 'eggs' represents the number of eggs you have to drop.

def find_highest_floor(building,eggs):

    define a variable that stores the number of eggs dropped. we'll call this 'dropped'

    dropped = 0

    define a function to drop an egg. each time this function is called it decrements the number of eggs you have and increments the number of eggs dropped.


    def drop_egg(e,d):
        e -= 1
        d += 1

    if the egg that is dropped breaks, the drop_egg() function will return a 1, otherwise it will return a 0.
 
        if egg breaks:
            return 1
        else:
            return 0

    on each floor, we drop one egg to see if it breaks. if it does we have our "N"
    the number of eggs dropped being returned will tell us the value of "n"/which floor
    otherwise if it doesnt break, go to the next floor.

    for floor in building:     O(n)
        drop_egg(eggs,dropped) O(1)
        if drop_egg() == 1:
            return dropped 
        else: 
            continue


time comploexity: O(n) * O(1) = O(n)

    



